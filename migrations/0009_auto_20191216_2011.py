# Generated by Django 2.2.6 on 2019-12-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_biodata', '0008_auto_20191216_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='handle',
            field=models.SlugField(blank=True, default=None, max_length=31, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('s', 'Sponsored'), ('c', 'Consultancy')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teachingengagement',
            name='student_count',
            field=models.IntegerField(blank=True),
        ),
    ]
