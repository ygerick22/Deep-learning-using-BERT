# Generated by Django 4.2 on 2023-04-24 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_acquired_skills_details_certifications_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='education',
            new_name='education_history',
        ),
    ]