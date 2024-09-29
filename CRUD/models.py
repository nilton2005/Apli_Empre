from django.db import models

# Create your models here.
class User(models.Model):
    #add fiel for id autoincrement  
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.username

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    city = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class RegisterEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username + ' - ' + self.event.title