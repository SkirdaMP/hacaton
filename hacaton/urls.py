from django.urls import path

from .views import ar_form

urlpatterns = [
    path('', ar_form, name='ar_form'),
]