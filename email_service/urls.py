from django.urls import path
from .views import email_verification,temp_details

urlpatterns=[
    path('send-mail/',email_verification),
    path('mail-employee-details/',temp_details)
]