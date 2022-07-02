import profile
from tokenize import blank_re
from django.urls import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm,ProfileForm,UserForm

def registerPage(request):
    if request.user.is_authenticated:#if the user is authenticated directly redirects to the profile which is having basuc values
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method == 'POST':#else the values are being taken from the form which is already defined in the forms.py and then checking for the validations provided by django authentication
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()#if the form is valid the values are being saved to database
                user = form.cleaned_data.get('firstname')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)#if the form is not valid the registerpage will get redirected

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password =request.POST.get('password')

            user = authenticate(request, email=username, password=password)#checking the logged values with values present in the database. If matched then it move forard to login

            if user is not None and user.last_login is None:
                auth_login(request,user)#if the user is logging in for the first time the user is getting mapped to the profile user
                user1=request.user
                x=Profile(user=user1,profile_image='download.png')
                print(x)
                x.save()
                return redirect('profile')
            elif user is not None and user.last_login is not None:#if the user is not logging in for the first time directly goes to profile page after logging in
                auth_login(request,user)
                return redirect('profile')
            else:
                messages.info(request, 'Username OR password is incorrect')#if the user is not found in the database throws error
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):#for logging out
	logout(request)
	return redirect('login')


def ProfileView(request):#this is just to view the details of the user
    user1=request.user   
    context={'user':user1}
    return render(request, 'accounts/profile.html',context)


class ProfileUpdateView(LoginRequiredMixin, TemplateView):#this view is helpful in updating the values and saving it to the database
    user_form = UserForm
    profile_form = ProfileForm #these two forms helps in updating basic details and also profile details
    template_name = 'accounts/profile-update.html'#

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)#takes the values from userform
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)#takes the values from profile form

        if user_form.is_valid() and profile_form.is_valid():#validating the forms whether they are correct or not
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))#returns to profile page

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     #the context data is used for displaying the content in the html/template

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def registration(request):#this form is for admin registration
    global p
    if request.method=='POST':#taking in the values from the template
        user=Admin()
        user.Username=request.POST['username']
        user.email=request.POST['email']
        user.password=request.POST['password']
        user.conformpassword=request.POST['confirm-password']
        p=1
        if user.Username=='' or user.email=='' or user.password=='' or user.conformpassword=='':
            p=0
            messages.add_message(request, messages.WARNING, 'Some fields are empty.Please fill all the fields and click on "Register Now"')
            return redirect('registerAdmin')

        if user.password!=user.conformpassword:#validating password with confirm password
            p=0
            messages.add_message(request, messages.WARNING, 'Password and confirm Password did not match. Please try again')
            return redirect('registerAdmin')
        x=Admin.objects.all()
        for i in x:
            if i.email==user.email:
                messages.add_message(request, messages.WARNING, 'Email already exists.Please try again')
                p=0
        if(p==1):
            user.save()
            return redirect('loginAdmin')
    return render(request,'accounts/registerAdmin.html')
			


def login(request):
    global p2
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        x=Admin.objects.all()
        for i in x:
            p2=0
            if i.email==email and i.password==password:#checking for the mapping values existing in database .If present then redirecting to home page
                p2=1
                return redirect('home')
        if(p2!=1):
            messages.error(request, "Bad Credentials!!")
            return redirect('loginAdmin')
    
    return render(request, "accounts/loginAdmin.html")

def home(request):#list of all the users who are created their accounts
    books = User.objects.all()
    return render(request, 'accounts/home.html', {'books':books})

def disable(request,pk):#if the admin clicks on block then the user accound will get disabled
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect('home')

def viewUser(request,pk):#viewing the particular user details
    user = User.objects.get(id=pk)
    context={'user':user}
    return render(request, 'accounts/view.html',context)












