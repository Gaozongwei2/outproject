# Generated by Django 2.1.2 on 2018-10-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.TextField(null=True),
        ),
    ]