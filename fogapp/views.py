from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Profile,File_Save


def home(request):
    return render(request, "./home.html")


def register(request):
    return render(request, "./register.html")


def login_view(request):
    return render(request, "./login.html")


def logout_user(request):
    logout(request)
    return redirect(reverse('home'))


def dashboard(request):
    if request.user.is_authenticated:
        user1 = User.objects.get(username=request.user)
        print(user1)
        pro = Profile.objects.get(user=user1)

        if pro.user_type == 0:
            return render(request, "./fileupload.html", {'username': user1.username})
        elif pro.user_type == 1:
            return HttpResponse("<h1>Cloud user</h1>")
        else:
            return HttpResponse("<h1>fog user</h1>")
    else:
        return redirect(reverse('login'))


def fileupload(request):
    if request.user.is_authenticated:
        print(request.user)
        return render(request, "./fileupload.html", {'username': request.user})



def table(request):
    files = File_Save.objects.filter(user=request.user)
    allFiles=[]
    for i in files:
        allFiles.append(i)
    return render(request, "./table.html", {'files': allFiles})


def user_registration(request):
    print("In User Registration")

    if request.method == 'POST':
        email_id = request.POST.get('email')
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('usertype')
        user = User.objects.create_user(username=user_name, email=email_id, password=password)
        user.save()
        profile = Profile(user=user, user_type=user_type)
        profile.save()
        login(request, user)

        return redirect(reverse('fileupload'))
    else:
        return redirect(reverse('login'))


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return redirect(reverse("register"))


def save_file(request):
    if request.method == 'POST':
        user = request.user
        file = request.POST.get('my-file')
        saveFiles = File_Save(user=user, file=file)
        saveFiles.save()
        return redirect(reverse('table'))
    pass
