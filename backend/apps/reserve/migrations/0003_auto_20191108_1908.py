# Generated by Django 2.2.5 on 2019-11-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_auto_20191108_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
