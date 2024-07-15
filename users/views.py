from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model

def signup(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            if User.objects.filter(username=name).exists():
              
                return render(request, 'users/signup.html', {'error_message': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
              
                return render(request, 'users/signup.html', {'error_message': 'Email already exists'})
            else:
                user = User.objects.create_user(username=name, email=email)
                user.set_password(pass1)
                user.save()
               
                return redirect('login')
        else:
            return render(request, 'users/signup.html', {'error_message': 'Passwords do not match'})

    return render(request, 'users/signup.html')

def login(request):

    if request.user.is_authenticated:
        print('if auth')
        return redirect('store')

    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        # Get the user by email
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = None

        if user is not None:
            user = authenticate(request, username=user.username, password=pass1)
            if user is not None:
                auth_login(request, user)

                return redirect('store')

        return render(request, 'users/login.html', {'error_message': 'Bad Credentials'})
   
    return render(request, "users/login.html")

def logout(request):
    auth_logout(request)
    print('logout')
    return redirect('login')