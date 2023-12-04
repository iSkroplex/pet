from . import views
from django.urls import path

from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts')
]
