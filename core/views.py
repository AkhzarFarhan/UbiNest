from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Task, FinancialTransaction, SavingsGoal, GroupChat, Message, Event
from .forms import ProfileForm, TaskForm, FinancialTransactionForm, SavingsGoalForm, MessageForm



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'core/login.html'


@login_required
def homepage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    tasks = Task.objects.filter(assigned_to=request.user).order_by('due_date')[:5]  # Show 5 upcoming tasks
    transactions = FinancialTransaction.objects.filter(user=request.user).order_by('-date')[:5]  # Last 5 transactions
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    events = Event.objects.filter(participants=request.user).order_by('date')[:5]  # Show 5 upcoming events
    chats = GroupChat.objects.filter(members=request.user)

    context = {
        'profile': profile,
        'tasks': tasks,
        'transactions': transactions,
        'savings_goals': savings_goals,
        'events': events,
        'chats': chats,
        'avatar_url': profile.avatar.url if profile.avatar and hasattr(profile.avatar, 'url') else None,
    }
    return render(request, 'core/homepage.html', context)


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/profile.html', {'form': form, 'profile': profile})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'core/create_profile.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'core/task_list.html', {'tasks': tasks})



@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form})



@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'core/task_form.html', {'form': form})



@login_required
def finance_list(request):
    transactions = FinancialTransaction.objects.filter(user=request.user)
    return render(request, 'core/finance_list.html', {'transactions': transactions})



@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = FinancialTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('finance_list')
    else:
        form = FinancialTransactionForm()
    return render(request, 'core/transaction_form.html', {'form': form})



@login_required
def group_chat(request, group_id):
    group = GroupChat.objects.get(id=group_id)
    messages = group.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.group = group
            message.save()
            return redirect('group_chat', group_id=group.id)
    else:
        form = MessageForm()
    return render(request, 'core/group_chat.html', {'group': group, 'messages': messages, 'form': form})


@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {'events': events})
