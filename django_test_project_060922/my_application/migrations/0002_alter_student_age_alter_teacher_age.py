# Generated by Django 4.1.1 on 2022-09-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]