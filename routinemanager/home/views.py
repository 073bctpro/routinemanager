from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import RoutineForm, UserForm
from .models import Programs, Rooms, Routine, Subjects, Teachers, Users


def create_routine(request):
    form = RoutineForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        routine = form.save(commit=False)

        routine.save()
        return render(request, 'home/detail.html', {'routine': routine})
    context = {
        "form": form,
    }
    return render(request, 'home/create_routine.html', context)


def delete_routine(request, routineid):
    routine = Routine.objects.get(pk=routineid)
    routine.delete()
    return render(request, 'home/detail.html')


def detail(request, routineid):
    user = request.user
    routine = get_object_or_404(Routine, pk=routineid)
    return render(request, 'home/detail.html', {'routine': routine, 'user': user})


def index(request):
    return render(request, 'home/index.html')


def programs(request):
    return render(request, 'home/programs.html')


def subjects(request):
    return render(request, 'home/subjects.html')


def departments(request):
    return render(request, 'home/departments.html')


def teachers(request):
    return render(request, 'home/teachers.html')


def rooms(request):
    return render(request, 'home/rooms.html')

