from django import forms
from django.contrib.auth.models import User
from .models import Programs, Rooms, Routine, Subjects, Teachers, Users


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RoutineForm(forms.ModelForm):

    class Meta:
        model = Routine
        fields = []


class ProgramsForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = []


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = []


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = []


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = []