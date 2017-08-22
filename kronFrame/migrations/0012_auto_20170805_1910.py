# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-05 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kronFrame', '0011_auto_20151215_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_acronym',
            new_name='acronym',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_ID',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_credits',
            new_name='credits',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.IntegerField(choices=[(1, 'CSE'), (2, 'ECE'), (3, 'MTH'), (4, 'HSS'), (5, 'BIO'), (6, 'ECO'), (7, 'OTH')], default=1),
        ),
        migrations.AddField(
            model_name='course',
            name='choice_type',
            field=models.IntegerField(choices=[(1, 'Mandatory'), (2, 'Elective')], default=2),
        ),
        migrations.AddField(
            model_name='offered',
            name='class_type',
            field=models.IntegerField(choices=[(1, 'Lecture'), (2, 'Tutorial'), (3, 'Lab')], default=1),
        ),
        migrations.AddField(
            model_name='prerequisites',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prereqs', to='kronFrame.Course'),
        ),
        migrations.AddField(
            model_name='prerequisites',
            name='prerequisite',
            field=models.ManyToManyField(to='kronFrame.Course'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='kronFrame.Course'),
        ),
    ]