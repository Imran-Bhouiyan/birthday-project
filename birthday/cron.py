import logging 
logger = logging.getLogger(__name__)

from .models import *
from django.utils import timezone
from django.core.mail import send_mail

def my_scheduled_job():

    queryset = Customer.objects.filter(birthdate__day=timezone.now().date().day, birthdate__month=timezone.now().date().month)
    for customer in queryset:
        subject = 'Happy Birthday!'
        message = f'Hi {customer.full_name},\n\nHappy birthday! Wishing you a fantastic day ahead!'
        from_email = 'imranpassw0rd@gmail.com'
        recipient_list = [customer.email]
        send_mail(subject, message, from_email, recipient_list)

    
    print("________________________________________________________________________________________________________________________________________")
    logger.info("corn Job was called")