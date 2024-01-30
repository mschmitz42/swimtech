from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


def user_is_staff(user):
    return user.is_staff


def swimtech_index(request):
    return render(request, 'swimtech/index.html')


@login_required
@user_passes_test(user_is_staff)
def dashboard(request):
    return render(request, 'swimtech/dashboard.html')
