from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.auth import login, authenticate
def logg(request):
    context = {
        'form':UserForm(),
        'errors':[]
    }
    if request.method =="POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('polls')
        else:
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
                user = User.objects.create_user(request.POST['first_name'],request.POST['email'],request.POST['password'])
                user.first_name=user.username
                user.username = request.POST['email']
                user.save()
                return redirect('logg')
            else:
                context['errors'].append("Passwords aren't matching!")
                return render(request, 'Authorization/register.html', context)
    else:
        context['errors'].append("Please, fill the form below.")
        return render(request, 'Authorization/register.html', context)
    return render(request, 'Authorization/register.html', context)
