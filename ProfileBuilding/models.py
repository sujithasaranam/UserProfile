from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):#to login using email instead of username the class is written to ovverride the base class
    def _create_user(self,email,password,firstname,lastname,**extra_fields):#fields that we gonna add newly are described
        if not email:#if email is blank the error will be raised
            raise ValueError("Email must be provided")
        if not password:#if password is blank the error will be raised
            raise ValueError("password is not provided")

        user= self.model(#the fields in user model are described here
            email= self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )

        user.set_password(password)#password will be there in django authentication system and that is being set
        user.save(using=self._db)
        return user

    def create_user(self,email,password,firstname,lastname,**extra_fields):#these fields are the existing fields if the user is not superuser. Since we have created new user we are also overriding create user
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,firstname,lastname,**extra_fields)
    
    def create_superuser(self,email,password,firstname,lastname,**extra_fields):#these fields are for superuser
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,firstname,lastname,**extra_fields)

    

class User(AbstractBaseUser,PermissionsMixin):#Inheriting the base user properties using Mixin. Mixin is helpful for inheriting parent properties
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(db_index=True,unique=True,max_length=254)
    is_staff= models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='email'#username field is being replaced with email
    REQUIRED_FIELDS=['firstname','lastname']#marking these fields as required fields

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'


class Profile(models.Model): #this is another model to update profile as instructed 
    user = models.OneToOneField(User, on_delete=models.CASCADE)#onetoone field is created to map the values for the user model
    profile_image = models.ImageField(upload_to='users/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number=models.CharField(max_length=10,null=True)
    course_name=models.TextField(max_length=500, blank=True)
    course_duration=models.IntegerField(default=0,null=True)
    course_passoutyear=models.CharField(max_length=4,null=True)
    course_percentage=models.FloatField(default=0,null=True)
    company_name=models.CharField(max_length=100,null=True, blank=True)
    duration=models.IntegerField(default=0,null=True)
    job_description=models.TextField(max_length=500, blank=True)
    salary=models.IntegerField(default=0,null=True)
    project_name=models.CharField(max_length=100,null=True, blank=True)
    duration_project=models.IntegerField(default=0,null=True)
    project_description=models.TextField(max_length=500, blank=True)
    role=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return '%s %s' % (self.user.firstname, self.user.lastname)

class Admin(models.Model):#admin model for viewing the details of the user and blocking the user
    Id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    conformpassword=models.CharField(max_length=20)


    def __str__(self):
        return '%s' % (self.Username)
# Create your models here.
