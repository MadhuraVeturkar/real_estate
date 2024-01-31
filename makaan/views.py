from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def add_property(request):
    return render(request,'add_property.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})


def signup(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']
        
        if User.objects.filter(username=email).exists():
            # user already exist
            return redirect('/signup')
        else:
            user = User.objects.create_user(username=email,password= password, email=email, first_name=name)
            user.save()
            # user created
            return redirect('/login')
    else:
        return render(request, "sign_up.html", {})

def login(request):
    if request.method== "POST":
        email = request.POST['email']
        password = request.POST['pwd']
        user= auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request,user)
            print(f"User {email} is logged in")
            return redirect("/")
        else:
            print("Invalid Login detaisl")
            return redirect("/login")
    else:
        return render(request, "login.html",{})
    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")

