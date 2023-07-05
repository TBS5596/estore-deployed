# Generated by Django 4.2.2 on 2023-07-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
