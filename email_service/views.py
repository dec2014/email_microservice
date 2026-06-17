from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .service import EmailVerification,TempEmployeeCredentials
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def email_verification(request):
    return EmailVerification(request)



@api_view(['POST'])
def temp_details(request):
    return TempEmployeeCredentials(request)