from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Task_Create
from datetime import date


# Create your views here.
@login_required(login_url='sign_in')
def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already exist")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Successfully SignUp')
                return redirect('sign_in')
        else:
            messages.info(request, 'Password Doesnot match **')
            return redirect('signup')

    return render(request, 'signup.html')

def sign_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Username Does not exit')
            return  redirect('sign_in')
        user =authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid password')
            return redirect('sign_in')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('sign_in')

def task_create(request):
    #date and time 
    try:
        if request.method=='POST':
            title =request.POST['title']
            description =request.POST['description']
            status =request.POST['status']
            assign_to = request.POST['assign_to']            
            deadline = request.POST['datetime']
            create = Task_Create(title=title,description=description,status=status,assign_to=assign_to,deadline=deadline)
            create.save()
            return redirect('taskview') 
    except:
        messages.info(request,'Please enter valid date and time')
        return redirect('taskcreate')

    members= User.objects.all()
    d=date.today()
    return render(request, 'task_create.html',{'members':members,'times':d})

def task_view(request):
    tasks = Task_Create.objects.all()
    return render(request, 'task_view.html',{'tasks':tasks})

def task_delete(request,id):
    t = Task_Create.objects.get(id=id)
    t.delete()
    return redirect('taskview')

def edit(request,id):
    try:
        if request.method=='POST':
            updata =Task_Create.objects.get(id=id)
            updata.title =request.POST['title']
            updata.description =request.POST['description']
            updata.status =request.POST['status']
            updata.assign_to = request.POST['assign_to']            
            updata.deadline = request.POST['datetime']
            updata.save()
            return redirect('taskview') 
        else:
            dt = Task_Create.objects.get(id=id)
    except:
        messages.info(request,'Please enter valid date and time')
        return redirect('taskcreate')
    members= User.objects.all()
    return render(request, 'edit.html',{'dt':dt,'members':members})
