from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    dfrom = models.DateField(auto_now=False, auto_now_add=False)
    dto = models.DateField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey('Location', related_name='project_location', on_delete=models.CASCADE)
    discription = models.TextField(max_length=3000)
    photo = models.ImageField(upload_to='project/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(null=True , blank=True)



    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)    
       super(Project, self).save(*args, **kwargs) # Call the real save() method
     

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 
    
        
    def get_absolute_url(self):
        return reverse('Projects:Projects', kwargs={'slug': self.slug})


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
    
    
    
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='projects_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/')

    def __str__(self):
        return str(self.project)