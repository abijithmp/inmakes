from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Details")
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['user_name']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        Cpassword=request.POST['password_1']
        if password==Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "Password Not Matching")
            print("not")
            return redirect('register')



    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

