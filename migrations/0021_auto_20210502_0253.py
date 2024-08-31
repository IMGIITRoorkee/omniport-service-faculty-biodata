# Generated by Django 3.0.3 on 2021-05-01 21:23

import common_biodata.utils.updated_URLValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_biodata', '0020_merge_20200918_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='personal_website',
            field=models.CharField(blank=True, max_length=255, validators=[common_biodata.utils.updated_URLValidator.UpdatedURLValidator()]),
        ),
    ]