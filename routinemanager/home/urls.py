from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view', views.detail, name='detail'),
    url(r'^create/$', views.create_routine, name='create_routine'),
    url(r'^delete/$', views.delete_routine, name='delete_routine'),
    url(r'^programs/$', views.programs, name='programs'),
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^departments/$', views.departments, name='departments'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^rooms/$', views.rooms, name='rooms'),
]
