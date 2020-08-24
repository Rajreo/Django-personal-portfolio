from django.db import models

# Create your models here.
class Blog_project(models.Model):
    Title=models.CharField(max_length=200)
    Description=models.CharField(max_length=400)
    Date=models.DateField()

    def __str__(self):
        return self.Title + "   "+str(self.Date)