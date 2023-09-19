from django.db import models

# Create your models here.


class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20,null = True)
    subject =models.TextField(max_length=200)
    message = models.TextField(max_length = 2000)
    date=models.DateField()
    file = models.FileField(blank=True,upload_to="files",default="")
 

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length = 200)
    date=models.DateField()

    def __str__(self):
        return self.email


class Getstarted(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    workemail =models.CharField(max_length = 30)
    phone = models.TextField(max_length= 20)
    message = models.TextField(max_length = 1100,default ='')
    date=models.DateField()

    def __str__(self):
        return self.firstname


