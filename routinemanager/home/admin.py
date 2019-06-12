from django.contrib import admin
from .models import Programs, Rooms, Routine, Subjects, Teachers

# Register your models here.
admin.site.register(Programs)
admin.site.register(Routine)
admin.site.register(Rooms)
admin.site.register(Subjects)
admin.site.register(Teachers)
