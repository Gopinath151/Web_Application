import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from Admin_web.models import Registration
from Admin_web.models import Admin_Login
from django.contrib import messages
# Create your views here.


def Login(request):

    global abc
    abc = {"username":"", "password":"", "loginStatus":""}
    return render(request,'Login_page.html')


def Admin_page(request):
    if request.method == 'POST':
        obj = Admin_Login.objects.create(App_name=request.POST.get('appName'),
                                     App_URL=request.POST.get('appIcon'),
                                     App_category=request.POST.get('appCategory'),
                                     Subcategory=request.POST.get('subCategory'),
                                     points=request.POST.get('points')
                                     )
        return HttpResponse("Application added successfully")
    return render(request, 'Admin.html')
    # if request.method=='POST':
    #     Imagefile = request.FILES['abcd']
    #     img_1 = str(request.FILES['abcd'])
    #     print(img_1)
    #     save_path = str(settings.MEDIA_ROOT)+'/admin_image//' + str(request.FILES['abcd'])
    #     print(save_path)
    #     path=default_storage.save(str(save_path),request.FILES['abcd'])


def User_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd= request.POST.get('password')
        print(uname)
        print(pwd)
        obj = Registration.objects.filter(
            username=uname,
            password=pwd
        )
        if len(obj)!=0:
            # abc = {"username": uname, "pass":pwd , "loginStatus":"true"}
            # request.session["User_session_ID"]= obj[0].id -dbt
            abc.update({"username": uname})
            abc.update({"password": pwd})
            abc.update({"loginStatus": "true"})
            return redirect('user_page')
        else:
            messages.warning(request, "Please provide Valid username or password")
            return redirect('User_login')
    return render(request, 'User_login_page.html')


def User_reg(request):
    if request.method=='POST':
        obj=Registration.objects.create(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            flag=1,
        )
        return redirect('User_login')
    return render(request,'User_registration.html')

def user_page(request):
    # if request.method=='POST' and 'myform' in request.method:
    #     Registration.objects.filter
    if request.method=='POST':
        Imagefile = request.FILES['abcd']
        img_1 = str(request.FILES['abcd'])
        print(img_1)
        save_path = str(settings.MEDIA_ROOT)+'/admin_image//' + str(request.FILES['abcd'])
        print(save_path)
        path=default_storage.save(str(save_path),request.FILES['abcd'])
        point = request.POST.get('Points')
        Registration.objects.filter(password=abc.get('password')).update(path=path)
        Registration.objects.filter(password=abc.get('password')).update(Points=point)

        return HttpResponse("points added successfully")

    if abc.get("loginStatus")=="" or abc.get("loginStatus")!="true":
        return redirect("Login")
    usname = abc.get('username')
    passd = abc.get('password')

    currentSession = Registration.objects.filter(username=usname,password=passd)

    #     Registration.objects.get(id=request.session["User_session_ID"])
    obj = Admin_Login.objects.all()


    return render(request,"User_page.html",{"sessionDetails":currentSession,"objects":obj})

# def appsession(request,pk):
#     if request.method =='POST' and 'mysession' in request.method:
#         session = Admin_Login.objects.get(App_name=pk)
#
#     return render(request,"User_page.html",{"appsession":session})

def logout(request):
     return render(request,'Login_page.html')



