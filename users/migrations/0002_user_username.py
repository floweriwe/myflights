# Generated by Django 5.1 on 2024-08-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=150, unique=True),
        ),
    ]
