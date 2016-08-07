from django.db import models
from django.forms import ModelForm

class User(models.Model):
    email = models.EmailField(null=False)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    userid = models.ForeignKey(User,null=False)
    date = models.DateField(null=False)
    task = models.CharField(max_length=50,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.task

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['date', 'task', 'userid']
