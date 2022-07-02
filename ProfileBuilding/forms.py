from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ProfileBuilding.models import User,Profile
from django import forms


class CreateUserForm(UserCreationForm):#this is for registration and login purpose. we are using the fields from this form
    email=forms.EmailField(max_length=254)#defining the extra fields which are not there in the default form
    firstname=forms.CharField(max_length=100)
    lastname=forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['email','firstname','lastname', 'password1', 'password2']#specifying the fields of the form

class UserForm(forms.ModelForm): #for updating the profile we have used this form to update these values.
    class Meta:
        model = User
        fields = [
            'firstname', 
            'lastname', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):#for updating profile all the fields are taken from Profile model and was being used while updating the Profile
    class Meta:
        model = Profile
        fields = ['user','profile_image','bio','phone_number','course_name','course_duration',
                    'course_passoutyear','course_percentage','company_name','duration','job_description',
                    'salary','project_name','duration_project','project_description','role']

