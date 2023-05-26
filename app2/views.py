from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<center><h1><i>Virat is a run machine</i></h1></center>')
def hardik(request):
    return HttpResponse('<center><h2><i>Hardik is a best all rounder</i></h2></center>')
def rohit(request):
    return HttpResponse('<center><h1><i>Rohit is a present Indian captain</i><h1></center>')