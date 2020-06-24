# Generated by Django 2.2.6 on 2020-06-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_biodata', '0011_auto_20200622_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='level',
            field=models.CharField(choices=[('ug', 'Undergraduate'), ('pg', 'Postgraduate'), ('phd', 'PhD'), ('rp', 'Research Project'), ('oth', 'Other')], default='oth', max_length=3),
        ),
        migrations.AddField(
            model_name='supervision',
            name='phd_type',
            field=models.CharField(blank=True, choices=[('f', 'Fulltime'), ('p', 'Parttime')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='teachingengagement',
            name='semester',
            field=models.CharField(choices=[('s', 'Spring'), ('a', 'Autumn')], default='s', max_length=1),
        ),
    ]
