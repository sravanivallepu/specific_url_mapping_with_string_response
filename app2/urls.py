from django.urls import path
from app2.views import *
app_name='something'

urlpatterns = [
    path('virat/',virat,name='virat'),
    path('hardik/',hardik,name='hardik'),
    path('rohit/',rohit,name='rohit'),
]