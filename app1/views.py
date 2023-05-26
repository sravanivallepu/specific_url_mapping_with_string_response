from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<center><h1><i>MSD is a best captain</i></h1></center>')
def hardik(request):
    return HttpResponse('<center><h2><i>Hardik is a best all rounder in Indian team</i></h2></center>')
def raina(request):
    return HttpResponse('<center><h1><i>Raina is a Mr IPL</i><h1></center>')