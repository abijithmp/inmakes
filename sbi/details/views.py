
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import Person, Branch,District

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


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    return render(request, 'about.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})


def wikipedia(request,district_id):
    district=District.objects.get(id=district_id)
    return render(request,'wiki.html',{'district':district})
