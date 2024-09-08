from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    stat_list = (
        ('talent', 'Talent'),
        ('client', 'Client')
    )
    status = models.CharField(max_length=30, choices=stat_list, default='Who are you ?')

    def __str__(self):
        return self.user.username

class PostJob(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    budget = models.IntegerField()
    tag_list = (
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('python', 'Python')
    )
    tags = models.CharField(max_length=50, choices=tag_list, default='Select Tags')
    time_posted = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job_title = models.CharField(max_length=1000)
    job_author = models.CharField(max_length=300, null=True)
    bid = models.IntegerField(null=True)
    cover_letter = models.TextField(max_length=1000)
    applicant_name = models.CharField(max_length=100)
    #hired = models.BooleanField()

    def __str__(self):
        return self.applicant_name