from django.urls import reverse
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login



class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

    def get_success_url(self):
        return reverse('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


def store(request):
    return render(request,'store/main.html')
     
def signup(request) :

    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if pass1 == pass2:
            if User.objects.filter(username=name).exists() :
                messages.error(request,"Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")

            else :
                user = User.objects.create_user(username=name,email=email)
                user.set_password(pass1)
                user.save()
                messages.success(request, "Your account has been successfully created")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'users/signup.html')



def login(request) :
    if request.method =='POST' :
        name = request.POST.get('name')
        pass1 = request.POST.get('pass1')

        #inbuild 
        user = authenticate(request,username=name,password=pass1)

        if user is not None :
            auth_login(request, user )
            return redirect('store')
        
        else :
            messages.error(request,"Bad Credintial...!!!")
            return redirect('login')
    


    return render(request,"users/login.html")




