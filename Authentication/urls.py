from django.urls import path
from Authentication import views as Authenticated_users
from rest_framework.authtoken import views as special_views

urlpatterns = [
    path('registration', Authenticated_users.registration_view,name="registration"),
    path('verification', Authenticated_users.verification_view,name="verification"),
    path('user_profile',Authenticated_users.get_profile,name="user_profile"),
    path('username',Authenticated_users.username_view,name="username")
    
]