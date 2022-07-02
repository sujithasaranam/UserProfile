from django.urls import path
from . import views
from ProfileBuilding.views import ProfileUpdateView

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('registerAdmin/', views.registration, name="registerAdmin"),
	path('loginAdmin/', views.login, name="loginAdmin"),  
	path('logout/', views.logoutUser, name="logout"),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', views.ProfileView, name='profile'),
    path('home/', views.home, name='home'),
    path('viewUser/<pk>',views.viewUser,name="viewUser"),
    path('disable/<pk>',views.disable,name="disable"),

]