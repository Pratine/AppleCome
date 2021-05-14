import os

from django.core.mail import send_mail
from django.shortcuts import render
import urllib
import json
from decouple import config

# Create your views here.
from django.template.loader import render_to_string, get_template


def home(request):
    if request.method == "POST":

        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': config('RECAPTACHA_SECRET'),
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        json.loads(response.read().decode())

        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        send_mail(
            "A empresa:" + message_name + " enviou uma mensagem atraves do site!",
            "A empresa da que enviou foi: " + message_name + 
            "\nA mensagem é: " + message,
            message_email,
            ['geral@appleCome.com'],
            fail_silently=True,
        )
        return render(request, 'home.html', {})

    else:
        return render(request, 'home.html', {})


def privacy_policy(request):
    return render(request, 'privacy_policy.html', {})
