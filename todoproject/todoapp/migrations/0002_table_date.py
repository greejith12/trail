# Generated by Django 4.2.8 on 2023-12-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='date',
            field=models.DateField(default='1999-02-02'),
            preserve_default=False,
        ),
    ]
