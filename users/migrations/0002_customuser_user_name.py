# Generated by Django 3.0.6 on 2020-12-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
