from asyncore import poll
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import PollForm
from .models import Poll

# Create your views here.
def home(request):
    poll_list = Poll.objects.all()
    total_polls = poll_list.count()
    context = {'poll_list': poll_list, 'total_polls': total_polls}
    return render(request, 'base/home.html', context)

def create(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/create.html', context)

def vote(request, poll_slug):
    poll = Poll.objects.get(question_slug=poll_slug)
    submit_succeed = False
    if request.method == 'POST':
        answer_selected = request.POST.get('poll')
        if answer_selected == 'option1':
            poll.question_one_count += 1
            submit_succeed = True
        elif answer_selected == 'option2':
            poll.question_two_count += 1
            submit_succeed = True
        elif answer_selected == 'option3':            
            poll.question_three_count += 1
            submit_succeed = True
        else:
            messages.error(request, 'Please select your answer')

        if submit_succeed:
            poll.save()        
            return redirect('result', poll.question_slug)
    
    context = {'poll': poll}
    return render(request, 'base/vote.html', context)

def result(request, poll_slug):
    poll = Poll.objects.get(question_slug=poll_slug)
    
    context = {'poll': poll}
    return render(request, 'base/result.html', context)

def edit(request, poll_slug):
    poll = Poll.objects.get(question_slug=poll_slug)
    form = PollForm(instance=poll)
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES, instance=poll)
        if form.is_valid():
            messages.success(request, 'Successfully edited')
            form.save()
            return redirect('home')

    context = {'poll': poll, 'form': form}
    return render(request, 'base/edit.html', context)

def delete(request, poll_slug):
    Poll.objects.get(question_slug=poll_slug).delete()
    return redirect('home')