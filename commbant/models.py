from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    id = models.IntegerField(unique = True, primary_key = True)
    name = models.TextField(unique = True) #Unique name to display
    members = models.ManyToManyField(User, related_name = "member")
    moderator = models.ForeignKey(User, related_name = "mode")

#class MyUser(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    #picture
    #some other useful stuff

class Msg(models.Model):
    user = models.TextField()
    group = models.ForeignKey(Group, related_name = "messages")
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {user}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'user': self.user, 'message': self.message, 'timestamp': self.formatted_timestamp}
