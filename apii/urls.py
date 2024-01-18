# apii/urls.py

from django.urls import path
from .views import  get_all_forms

urlpatterns = [
    #path('forms/<int:form_id>/', get_forms, name='get_forms'),
    path('get_all_forms/', get_all_forms, name='get_all_forms'),
]
