# Generated by Django 4.2 on 2023-04-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_requirementsinput_years_of_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='years_of_experience',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
