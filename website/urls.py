from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('jobs.html', views.jobs, name="jobs"),
    path('contact.html', views.contact, name="contact"),

]
