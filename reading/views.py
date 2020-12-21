from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "reading/index.html")

def about(request, r_Name, r_Id):
    return HttpResponse(f'{r_Name} {r_Id} TO DO')