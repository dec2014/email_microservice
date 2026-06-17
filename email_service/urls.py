from django.urls import path
from .views import email_verification

urlpatterns=[
    path('send-mail/',email_verification)
]