from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login 


def store(request):
    return render(request,'store/main.html')
     
def signup(request) :

    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if pass1 == pass2:
            my_user = User.objects.create_user(username=name, email=email, password=pass1)
            my_user.save()

            messages.success(request, "Your account has been successfully created")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'users/signup.html')



def login(request) :
    if request.method =='POST' :
        name = request.POST('name')
        pass1 = request.POST('pass1')

        #inbuild 
        user = authenticate(name=name,password=pass1)

        if user is not None :
            login(request, user )
        
        else :
            messages.error(request,"Bad Credintial...!!!")
            return redirect('store')
    


    return render(request,"users/login.html")




