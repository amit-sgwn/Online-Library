from django.shortcuts import render
from django.conntrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")