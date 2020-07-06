# Generated by Django 3.0.3 on 2020-07-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_biodata', '0015_auto_20200705_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachingengagement',
            name='lecture_hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachingengagement',
            name='practical_hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachingengagement',
            name='student_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachingengagement',
            name='tutorial_hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
