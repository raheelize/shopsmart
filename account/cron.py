from webservices.scrapeitems.sales import get_sales
from webservices.scrapeitems.fetch import update_products
from django.core.mail import send_mail
from account.models import Account
def updation():
    get_sales()
    update_products()
    emails = Account.objects.values_list('email',flat=True).distinct()
    for address in emails:
        email = EmailMessage('SHOPSMART',
                             'New Products of your interest have arrived! Check now on www.shopsmart.com',
                             'noreplyshopsmart@gmail.com',
                             [address],
                             fail_silently=False,
                             )
        email.send()
    #print("Printed From Cron Tab")