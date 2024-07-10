from django.shortcuts import render
from .models import Contact

def HomePage (request):
    return render(request,'HomePage.html')

def About (request):
    return render(request,'About.html')

def Experiences (request):
    return render(request,'Experiences.html')

def Achievements  (request):
    return render(request,'Achievements.html')

def Contacts  (request):
    if request.method=='POST':
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']
        
        contact = Contact(email=email, firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, message=message)
        contact.save()
        print("contact has been submitted")

    return render(request,'Contacts.html')