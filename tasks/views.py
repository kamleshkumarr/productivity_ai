from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Task, DailyActivity
from django.utils import timezone
from .forms import TaskForm
from ai.utils import get_ai_priority
from .utils import get_streak, get_motivation

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')   # ✅ only once
    return render(request, 'home.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    pending_tasks = tasks.filter(completed=False)
    completed_tasks = tasks.filter(completed=True)
    streak = get_streak(request.user)
    motivation = get_motivation(streak)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
        'streak': streak,
        'motivation': motivation
    })
    


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user

            # AI PRIORITY
            task.priority = get_ai_priority(
                task.title,
                task.description
            )

            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')   # ✅ only once
    return render(request, 'home.html')

# # MARK COMPLETE / INCOMPLETE TOGGLE
# @login_required
# def complete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id, user=request.user)
#     task.completed = not task.completed
#     task.save()
#     return redirect('dashboard')


# DELETE TASK
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')


# UPDATE TASK
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)

            # AI priority re-evaluation
            updated_task.priority = get_ai_priority(updated_task.title)

            updated_task.save()
            return redirect('dashboard')

    else:
        form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})

#Streaks and Daily Activity Tracking
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()

    today = timezone.now().date()

    activity, created = DailyActivity.objects.get_or_create(
        user=request.user,
        date=today
    )

    activity.tasks_completed += 1
    activity.save()

    return redirect('dashboard')