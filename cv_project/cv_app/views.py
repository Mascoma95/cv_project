from django.shortcuts import render
from .models import CV,Progetto
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    cv = CV.objects.all()
    progetti = Progetto.objects.all()
    return render(request,'cv_app/home.html', {'cv' : cv , 'progetti':progetti})

# Create your views here.
def thanks_view(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        recipients = ['mascomafederico@gmail.com']
        recipients.append(sender)
        try:
            send_mail(subject, message, sender, recipients)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request , 'cv_app/thanks.html/' , {'object' : {"name":name , "email" : sender}})
    else:
        form = ContactForm()
        return render(request,'cv_app/thanks_failed.html/')