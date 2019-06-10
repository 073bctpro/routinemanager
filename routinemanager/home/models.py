from django.db import models
from datetime import datetime, timedelta


def get_default_my_date():
    return datetime.now()


class Departments(models.Model):
    departmentid = models.CharField(db_column='DepartmentID', primary_key=True, max_length=2, blank=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=22, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'departments'


class Programs(models.Model):
    departmentid = models.ForeignKey(Departments, db_column='DepartmentID', on_delete=models.CASCADE)  # Field name made lowercase.
    programid = models.CharField(db_column='ProgramID', primary_key=True, max_length=3)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'programs'


class Rooms(models.Model):

    departmentid = models.ForeignKey(Departments, db_column='DepartmentID', on_delete=models.CASCADE)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', primary_key=True, max_length=18)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'rooms'


class Subjects(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=13, primary_key=True, blank=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments, db_column='DepartmentID', on_delete=models.CASCADE)  # Field name made lowercase.
    tyear = models.CharField(db_column='TYear', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tpart = models.CharField(db_column='TPart', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'subjects'


class Teachers(models.Model):
    departmentid = models.ForeignKey(Departments, db_column='DepartmentID', on_delete=models.CASCADE)  # Field name made lowercase.
    teacherid = models.CharField(db_column='TeacherID', max_length=3, primary_key=True, blank=True)  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'teachers'


class Routine(models.Model):
    routineid = models.DateTimeField(default=get_default_my_date, db_column='RoutineId', primary_key=True)
    programid = models.ForeignKey(Programs, db_column='ProgramID', on_delete=models.CASCADE)  # Field name made lowercase.
    teacherid = models.ForeignKey(Teachers, db_column='TeacherID', on_delete=models.CASCADE)  # Field name made lowercase.
    subjectid = models.ForeignKey(Subjects, db_column='SubjectID', on_delete=models.CASCADE)  # Field name made lowercase.
    ltp = models.CharField(db_column='LTP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'routine'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True, default='')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'users'
