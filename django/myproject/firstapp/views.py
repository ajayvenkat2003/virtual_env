import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import student
def home(request):
    return render(request,'index.html',{'ans':'overview will be here'})

def submit(request):
    if request.method == 'POST':
        ans=request.POST['area']
        if ans.strip()=='':
            ans={'ans':'overview will be here.....'}
        else:
            ans={'ans':'iam bad'}
    return render(request,'index.html',ans)
