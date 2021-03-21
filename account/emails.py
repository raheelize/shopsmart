
MSG ="We Welcome you to SHOPSMART, we're bringing Pakistani Clothing Brands together at one place for your ease, so you can explore your favourite apparels in seconds!.\nHope Your Experience goes well.\n Visit Now: www.shopsmart.com \nContact: info@shopsmart.com"


from django.core.mail import EmailMessage
def welcome_mail(name,address):
    email = EmailMessage(subject='SHOPSMART', body='Greetings '+str(name)+MSG ,from_email='noreplyshopsmart@gmail.com', to=address)
    email.send()