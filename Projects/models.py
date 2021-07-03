from django.db import models
from django.utils.text import slugify
from django.urls.base import reverse

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    type = models.ForeignKey('Type', related_name='project_type', on_delete=models.CASCADE)
    cooperate = models.ManyToManyField('Cooperate')
    photo = models.ImageField(upload_to='Projects/images', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(null=True , blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)    
        super(Project, self).save(*args, **kwargs) # Call the real save() method     

    def __str__(self):
        return self.title

   
    def get_absolute_url(self):
        return reverse('Projects:Projects', kwargs={'slug': self.slug})


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
    
    
    
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='projects_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/')

    def __str__(self):
        return str(self.project)
    
    
class Cooperate(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)