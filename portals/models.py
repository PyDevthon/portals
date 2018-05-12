from django.db import models
import datetime

CHOICES = [('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others')]


class Discussions(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now())
    category = models.CharField(choices=CHOICES, max_length=50)

    def __str__(self):
        return self.name


