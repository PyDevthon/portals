# Generated by Django 2.0 on 2018-05-18 17:14

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 5, 18, 22, 44, 12, 545790))),
                ('category', models.CharField(choices=[('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others')], max_length=50)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 5, 18, 22, 44, 12, 545790))),
                ('votes', models.IntegerField(default=0)),
                ('replied_to', models.ManyToManyField(to='portals.Discussions')),
                ('voted_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
