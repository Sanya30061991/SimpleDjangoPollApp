from django.shortcuts import render, redirect
from .models import Poll
from .forms import PollForm
from django.contrib.auth import logout
# Create your views here.
def loggggg(request):
    logout(request)
    return redirect('logg')

def show(request):
    polls = Poll.objects.all()
    context = {
        'errors' : [],
        'polls' : polls
    }
    return render(request, 'Main/show.html', context)