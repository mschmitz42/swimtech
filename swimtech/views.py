from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def swimtech_index(request):

    return render(request, 'swimtech/index.html')
