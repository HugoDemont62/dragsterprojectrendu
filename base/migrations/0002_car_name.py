# Generated by Django 5.0.4 on 2024-04-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(default='Default Name', max_length=255),
        ),
    ]
