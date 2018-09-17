from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.task_list),
    url(r'^post/new/$', views.task_new, name='task_new'),
]