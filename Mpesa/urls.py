from django.urls import path
import Mpesa.views as Mpesa

urlpatterns = [
    path("lipa",Mpesa.lipa_na_mpesa_online,name="lipa"),
    
]