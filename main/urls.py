from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name='home'),
    path('privacy_policy.html', views.privacy_policy, name="privacy_policy"),

]
