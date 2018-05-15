from django.db import models
import datetime
from django.contrib.auth.models import User

CHOICES = [('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others')]


class Discussions(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now())
    category = models.CharField(choices=CHOICES, max_length=50)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_replies(self):
        return self.replies_set.all()

# Replies will be to each Discussion items


class Replies(models.Model):
    replied_to = models.ManyToManyField(Discussions)
    content = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)

    def __str__(self):
        return self.content


# model for pusher

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)
    created_at = models.DateTimeField(auto_now=True)
