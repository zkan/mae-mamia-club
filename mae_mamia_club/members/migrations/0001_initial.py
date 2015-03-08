# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=300)),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=300)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('dad_name', models.CharField(max_length=300)),
                ('mom_name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('province', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to = 'kid_images/', default = 'kid_images/None/no-img.jpg')),
                ('facebook_account', models.CharField(max_length=300)),
                ('signup_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
