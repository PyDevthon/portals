# Generated by Django 2.0 on 2018-05-12 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discussions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 5, 12, 14, 26, 25, 979398))),
                ('category', models.CharField(choices=[('QA', 'QA'), ('BA', 'BA'), ('DEV', 'DEV'), ('Others', 'Others')], max_length=50)),
            ],
        ),
    ]
