# Generated by Django 3.2.5 on 2024-07-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
