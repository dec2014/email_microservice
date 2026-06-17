from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError
import json
from rest_framework.response import Response

@csrf_exempt
def EmailVerification(request):
    try:



        data=json.loads(request.body)
        subject=data.get('subject')
        body=data.get('body')
        email_from=data.get('email_from')
        recipient_list=data.get('recipient_list')
        send_mail( subject, body, email_from, recipient_list )  
        return Response('mail sent')
    except Exception as e:
        raise ValidationError(f'the email could not be sent.{str(e)}')



@csrf_exempt
def TempEmployeeCredentials(request):
    try:
        data=json.loads(request.body)
        subject=data.get('subject')
        body=data.get('body')
        email_from=data.get('email_from')
        recipient_list=data.get('recipient_list')
    
        send_mail(subject,body,email_from,recipient_list)
    except Exception as e:
        raise ValidationError(f'the email could not be sent.{str(e)}')

