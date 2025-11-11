#from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Search(models.Model):
    title=models.CharField(max_length=20)
    images=models.ImageField(upload_to='', verbose_name='写真', blank=False, null=True)

    def __str__(self):
        return self.title
