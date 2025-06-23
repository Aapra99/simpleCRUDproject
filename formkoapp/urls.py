from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.options,name='options'),
    path('form?<str:type>',views.form,name='form'),
    path('submission/<str:fetch_all>',views.submission,name='submission'),
    path('submitted/',views.submitted,name='submitted')
]
