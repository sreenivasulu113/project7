from django.urls import path
from app1.views import *
app_name='archi'
urlpatterns=[
    path('string/',string,name='string'),
]