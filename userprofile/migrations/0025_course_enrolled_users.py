# Generated by Django 3.2.12 on 2022-04-16 23:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0024_auto_20220413_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled_users',
            field=models.ManyToManyField(blank=True, related_name='enrolled_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
