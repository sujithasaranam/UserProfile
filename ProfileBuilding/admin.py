from django.contrib import admin
from .models import Admin, User,Profile

# Register your models here.
admin.site.register(User)#if we redister models then only we can be able to view in the django admin pannel
admin.site.register(Profile)
admin.site.register(Admin)