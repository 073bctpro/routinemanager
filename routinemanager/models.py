# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departments(models.Model):
    departmentid = models.CharField(db_column='DepartmentID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=22, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departments'


class Programs(models.Model):
    departmentid = models.CharField(db_column='DepartmentID', max_length=2)  # Field name made lowercase.
    programid = models.CharField(db_column='ProgramID', max_length=3)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programs'


class Rooms(models.Model):
    departmentid = models.CharField(db_column='DepartmentID', max_length=2)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=18)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooms'


class Routine(models.Model):
    programid = models.CharField(db_column='ProgramID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    teacherid = models.CharField(db_column='TeacherID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.CharField(db_column='SubjectID', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ltp = models.CharField(db_column='LTP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'routine'


class Subjects(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=13, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tyear = models.CharField(db_column='TYear', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tpart = models.CharField(db_column='TPart', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'


class Teachers(models.Model):
    teacherid = models.CharField(db_column='TeacherID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
