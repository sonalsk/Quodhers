# Generated by Django 3.1 on 2020-11-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='NgoLogo',
            field=models.ImageField(default='', upload_to='../media'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
