from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views , models

app_name = 'projects'


urlpatterns = [
    path('', views.ProjectsList.as_view(), name='projects')
]
