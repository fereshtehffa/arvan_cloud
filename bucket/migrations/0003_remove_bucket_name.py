# Generated by Django 3.1.4 on 2021-01-02 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_bucket_prefix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucket',
            name='name',
        ),
    ]
