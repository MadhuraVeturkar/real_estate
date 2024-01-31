from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Properties

# Create your views here.
def index(request):
    properties = Properties.objects.all()
    return render(request,'index.html',{"properties":properties})

def add_property(request):
    if request.method == "POST" and request.FILES['image']:
        title = request.POST['title']
        description = request.POST['description']
        property_type = request.POST['type']
        status = request.POST['status']
        location = request.POST['location']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        floors = request.POST['floors']
        garages = request.POST['garages']
        area = request.POST['area']
        price = request.POST['price']
        map_link = request.POST['map_link']
        address = request.POST['address']
        image = request.FILES['image']

        new_pro = Properties.objects.create(title=title, description=description, property_type=property_type, property_status=status, location=location, bedrooms=bedrooms,bathrooms=bathrooms,floors=floors,garages=garages,area=area,price=price,map_link=map_link,address=address,image=image)

        print("New Property Created !!!",new_pro)

        return redirect('/add_property')
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

