
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
        path('', views.homepage),
        path('options/',include('formkoapp.urls'))
]
