from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from preciseweb.models import *
# from .forms import *
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail  
from django.core.mail import EmailMessage
from precisedata import settings 
import time 




# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,"index.html")
  
    if request.method == 'POST' and 'contact' in request.POST  :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        files = request.FILES['file']
        contact = Contact(name = name,email = email, phone = phone, subject = subject ,message = message,file = files, date = datetime.today())
        contact.save()
        time.sleep(2)
        return redirect('index')

    if request.method == 'POST' and 'newsletter' in request.POST :
        email = request.POST.get('email')
        newsletter = Newsletter(email = email,date = datetime.today())
        newsletter.save()
        time.sleep(6)
        return redirect('index')


def privacypolicy(request):
    if request.method == 'GET':
        return render(request,"privacypolicy.html")

    
def getstarted(request):
    if request.method == 'GET':
        return render(request,"getstarted.html")
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        workemail = request.POST.get('workemail')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        getstarted = Getstarted(firstname = firstname,lastname = lastname,workemail = workemail,phone=phone,message = message,date = datetime.today())
        getstarted.save()
        

        html_content = 'Name :' + firstname + lastname + ' Work email :' + workemail + ' Phone :'+ phone + ' Message :'+ message
        print(html_content)
        email = send_mail('testing',html_content, 'jenil.a@dgmarket.in',['jenil.a@globalecontent.com','akoliyajenil@gmail.com','akoliyajenil1@gmail.com'],fail_silently = False)
          
        try:
            import os
            from twilio.rest import Client
            account_sid = "ACf14a86a56550b279fff64a8394447a4e"
            auth_token = "384554193e62b8c75c444d0b3a01f2be"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body = html_content,
            from_="+13613155310",
            to="+918097024701"
            )
            print(message.sid)
        except:
            pass
            
        return redirect("getstarted")


def ecommerce(request):
    if request.method == 'GET':
        return render(request,"ecommerce.html")


def socialmedia(request):
    if request.method == 'GET':
        return render(request,"socialmedia.html")

def seo(request):
    if request.method == 'GET':
        return render(request,"seo.html")

def adtech(request):
    if request.method == 'GET':
        return render(request,"adtech.html")

def market(request):
    if request.method == 'GET':
        return render(request,"market.html")

def travel(request):
    if request.method == 'GET':
        return render(request,"travel.html")

def finance(request):
    if request.method == 'GET':
        return render(request,"finance.html")

def healthcare(request):
    if request.method == 'GET':
        return render(request,"healthcare.html")

def realestate(request):
    if request.method == 'GET':
        return render(request,"realestate.html")

def good(request):
    if request.method == 'GET':
        return render(request,"good.html")

def datasets(request):
    if request.method == 'GET':
        return render(request,"datasets.html")

def template(request):
    if request.method == 'GET':
        return render(request,"template.html")

def customizescraping(request):
    if request.method == 'GET':
        return render(request,"customizescraping.html")

def automation(request):
    if request.method == 'GET':
        return render(request,"automation.html")



        