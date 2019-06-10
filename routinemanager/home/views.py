from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import RoutineForm, UserForm
from .models import Programs, Rooms, Routine, Subjects, Teachers, Users


def create_routine(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
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
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        user = request.user
        routine = get_object_or_404(Routine, pk=routineid)
        return render(request, 'home/detail.html', {'routine': routine, 'user': user})


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        return render(request, 'music/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html')
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html')
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)

