# Generated by Django 2.2.1 on 2019-07-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
