from django.shortcuts import render, redirect
from .models import Poll
from .forms import PollForm
from django.contrib.auth import logout
# Create your views here.

def res(request):
    if request.method == "GET":
        id = request.GET['Results']
        poll = Poll.objects.get(id=id)
        context = {
            'poll':poll
        }
    return render(request, 'Main/result.html', context)

def vote(request):
    if request.method == "GET":
        id = request.GET['Vote']
        poll = Poll.objects.get(id=id)
        context = {
            'poll':poll,
            'errors':[]
        }
        return render(request, 'Main/vote.html', context)
    elif request.method == "POST":
        context = {
            'errors':[]
        }
        if "opt1" in request.POST:
            id = request.POST['opt1']
            poll = Poll.objects.get(id=id)
            poll.votes1 = poll.votes1+1
            poll.total = poll.total+1
            poll.save()
            context = {
                'poll':poll
            }
            return render(request, 'Main/result.html', context)
        elif "opt2" in request.POST:
            id = request.POST['opt2']
            poll = Poll.objects.get(id=id)
            poll.votes2 = poll.votes2+1
            poll.total = poll.total+1
            poll.save()
            context = {
                'poll':poll
            }
            return render(request, 'Main/result.html', context)
        elif "opt3" in request.POST:
            id = request.POST['opt3']
            poll = Poll.objects.get(id=id)
            poll.votes3 = poll.votes3+1
            poll.total = poll.total+1
            poll.save()
            context = {
                'poll':poll
            }
            return render(request, 'Main/result.html', context)
        else:
            context['errors'].append("Vote before submitting!")
            return render(request, 'Main/vote.html', context)

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