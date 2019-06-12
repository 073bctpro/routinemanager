from rest_framework import serializers
from .models import Departments, Programs, Rooms, Routine, Subjects, Teachers


class departmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = '__all__'


class programsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programs
        fields = '__all__'


class roomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = '__all__'


class routineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = '__all__'


class subjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'


class teachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'

