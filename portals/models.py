import datetime
from django.db import models
from django.contrib.auth.models import User

CHOICES = [('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others')]


class Discussions(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now())
    category = models.CharField(choices=CHOICES, max_length=50)
    date = models.DateField(blank=False, null=False, default=datetime.date.today())


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
    votes = models.IntegerField(default=0)
    voted_by = models.ManyToManyField(User)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies_by')

    def get_voted_by(self):
        return [x.id for x in self.voted_by.all()]

    def __str__(self):
        return self.content
