from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    print(date)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    def save(self, *args, **kwargs):
        vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
        self.date = timezone.now().astimezone(vn_tz)
        super(Message, self).save(*args, **kwargs)