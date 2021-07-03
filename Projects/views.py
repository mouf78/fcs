from django.shortcuts import render
from .models import Project
from django.views.generic import ListView , DetailView
import Projects
# Create your views here.


class ProjectsList(ListView):
    model = Project
    #template_name = 'projects/ProjectsList.html'
     
 
 
 
 
 

class ProjectsDetail(DetailView):
    pass