from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import departmentsSerializer, programsSerializer, roomsSerializer, routineSerializer, subjectsSerializer, teachersSerializer
from django.shortcuts import render, get_object_or_404
from .forms import RoutineForm, UserForm
from .models import Departments, Programs, Rooms, Routine, Subjects, Teachers


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
    programs = Programs.objects.all()
    context = {'programs': programs}
    return render(request, 'home/programs.html', context)

def subjects(request):
    subjects = Subjects.objects.all()
    context = {'subjects': subjects}
    return render(request, 'home/subjects.html', context)


def departments(request):
    departments = Departments.objects.all()
    context = {'departments': departments}
    return render(request, 'home/departments.html', context)


def teachers(request):
    teachers = Teachers.objects.all()
    context = {'teachers': teachers}
    return render(request, 'home/teachers.html', context)


def rooms(request):
    rooms = Rooms.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home/rooms.html', context)


