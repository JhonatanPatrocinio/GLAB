# Generated by Django 2.2.5 on 2019-11-09 00:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191105_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('de4e8664-6716-492b-925a-b8e02779bee1'), primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
