from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView  
from django.contrib.auth.views import LoginView
from . import views 

app_name = 'members'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name= 'registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),  
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('badge_success/<str:badge_name>/', views.badge_success, name='badge_success'),
    path('my_collection/', views.my_collection, name='my_collection'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),


]
