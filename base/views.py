from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import PollForm
from .models import Poll
from accounts.models import Profile

# Create your views here.
@login_required
def home(request):
    poll_list = Poll.objects.all().order_by('-id')
    current_user = request.user    
    poll_voted = Poll.objects.filter(voted=current_user) 
    one = []
    two = []
    for data in poll_list:
        one.append(data)
    for data in poll_voted:        
        two.append(data)    
    three = one + two
    polls = []
    for data in three:
        if data in two:
            continue
        polls.append(data)
    total_polls = poll_list.count()
    context = {'polls': polls, 'total_polls': total_polls}
    return render(request, 'base/home.html', context)

@login_required
def create(request):
    form = PollForm()
    profile_form = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.poll_creator = profile_form
            instance.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/create.html', context)
        
@login_required
def vote(request, poll_slug, poll_uuid):
    poll = Poll.objects.get(poll_uuid=poll_uuid)
    current_signed_in = request.user.profile.profile_uuid
    creator = poll.poll_creator.profile_uuid  
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
            poll.voted.add(request.user)
            poll.save()        
            return redirect('result', poll.question_slug, poll.poll_uuid)
    
    context = {'poll': poll, 'current_signed_in': current_signed_in, 'creator': creator}
    return render(request, 'base/vote.html', context)

@login_required
def result(request, poll_slug, poll_uuid):
    poll = Poll.objects.get(poll_uuid=poll_uuid)
    
    context = {'poll': poll}
    return render(request, 'base/result.html', context)

@login_required
def edit(request, poll_slug, poll_uuid):
    poll = Poll.objects.get(poll_uuid=poll_uuid)
    form = PollForm(instance=poll)
    current_signed_in = request.user.profile.profile_uuid
    creator = poll.poll_creator.profile_uuid    
    if request.method == 'POST':             
        form = PollForm(request.POST, request.FILES, instance=poll)
        if form.is_valid():
            messages.success(request, 'Successfully edited')
            form.save()
            return redirect('home')

    context = {'poll': poll, 'form': form, 'current_signed_in': current_signed_in, 'creator': creator}
    return render(request, 'base/edit.html', context)

@login_required
def clear_selected_count(request, poll_slug, poll_uuid):
    poll = Poll.objects.get(poll_uuid=poll_uuid)
    if poll.question_one_count == 0 and poll.question_two_count == 0 and poll.question_three_count == 0:        
        messages.error(request, 'Selected counts is already zero!')        
        return redirect('edit', poll.question_slug, poll.poll_uuid)
    else:
        poll.question_one_count = 0
        poll.question_two_count = 0
        poll.question_three_count = 0
        messages.success(request, 'Selected counts has been restart')        
        poll.save()
        return redirect('result', poll.question_slug, poll.poll_uuid)

@login_required
def delete(request, poll_slug, poll_uuid):
    Poll.objects.get(poll_uuid=poll_uuid).delete()
    return redirect('home')