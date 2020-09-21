from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title =models.CharField(max_length=50)
    date=models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:100]

   

    def __str__(self):
        return self.title