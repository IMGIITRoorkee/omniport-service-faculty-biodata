# Generated by Django 2.2.6 on 2019-12-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_biodata', '0006_auto_20191216_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativeposition',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
