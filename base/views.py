from django.shortcuts import render, HttpResponse

from .models import *

def landing(request):

    return render(request, 'landing.html')

def receive_contact_info(request):

    name = request.POST.get('n')
    phone = request.POST.get('p')

    Customer.objects.create(name = name, phone = phone)

    return HttpResponse('K')