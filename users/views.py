from django.shortcuts import render

def store(request):
    return render(request,'store/main.html')
     
def signup(request) :
    return render(request,'users/signup.html')

def login(request) :
    return render(request,"users/login.html")

