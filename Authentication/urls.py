from django.urls import path
from Authentication import views as Authenticated_users
from rest_framework.authtoken import views as special_views

urlpatterns = [
    path('registration', Authenticated_users.registration_view,name="registration"),
    path('verification', Authenticated_users.verification_view,name="verification"),
    
]