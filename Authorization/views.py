from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.auth import login
def logg(request):
    context = {
        'form':UserForm(),
        'errors':[]
    }
    if request.method =="POST":
        username = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user is not None and password==user.password and username==user.username:
            login(request, user)
            return redirect('polls')
        elif user is not None or user!=user.password:
            context['errors'].append("Invalid login or password.")
            return render(request, 'Authorization/login.html', context)
    else:
        context['errors'].append("Please, fill the form below.")
        return render(request, 'Authorization/login.html', context)
    return render(request, 'Authorization/login.html', context)

def regg(request):
    context = {
        'form':UserForm(),
        'errors':[]
    }
    if request.method =="POST":
        userss = User.objects.filter(email = request.POST['email'])
        if len(userss)!=0:
            context['errors'].append("User with this login already has been registered.")
            return render(request, 'Authorization/register.html', context)
        else:
            if request.POST['last_name']==request.POST['password']:
                form = UserForm(request.POST)
                return redirect('logg')
            else:
                context['errors'].append("Passwords aren't matching!")
                return render(request, 'Authorization/register.html', context)
    else:
        context['errors'].append("Please, fill the form below.")
        return render(request, 'Authorization/register.html', context)
    return render(request, 'Authorization/register.html', context)
