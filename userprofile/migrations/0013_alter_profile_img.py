# Generated by Django 3.2.12 on 2022-04-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_alter_profile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='userprofile\\templates\\userprofile\\icons\\profile.png', upload_to='images'),
        ),
    ]
