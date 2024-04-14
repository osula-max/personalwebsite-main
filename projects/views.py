
from projects.models import Project
from django.core.mail import send_mail
#from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse 
from django.shortcuts import render, redirect
from projects.forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage



def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'andrew.osula@yahoo.com', # Send from (your website)
               ['andrewosula@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})   


def success(request):
   return render(request, 'success.html')


#def contact(request):
    #if request.method == 'POST':
        #message_name = request.POST['message-name']
        #message_email = request.POST['message-email']
        #message = request.POST['message']
        
        #send_mail(
            #message_name, # subject
            #message_email, # from email
            #message, # message
            #['andrewosula@gmail.com'], # To Email
        #)
        #return redirect('success')     
        #return render(request, 'contact.html', {'message_name':message_name})
    #else:
        #form = ContactForm()
    #return render(request, 'contact.html', {'form': form})
    
#def success(request):
    #return render(request, 'success.html') 
    
#def contact(request):
    #if request.method == "POST":
        #form = ContactForm()
    #else:
        #form = ContactForm(request.POST)
        #if form.is_valid():
            #subject = form.cleaned_data["subject"]
            #from_email = form.cleaned_data["from_email"]
            #message = form.cleaned_data['message']
            #try:
                #send_mail(subject, message, from_email, ["andrewosula@gmail.com"])
            #except BadHeaderError:
                #return HttpResponse("Invalid header found.")
            #return redirect("success")
    #return render(request, "contact.html", {"form": form})

#def success(request):
    #return HttpResponse("Success! Thank you for your message.")

   
 
def cv(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'cv.html', context)  

def works(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'works.html', context)   









