# Generated by Django 2.2.5 on 2019-11-06 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratory',
            old_name='nome',
            new_name='name',
        ),
    ]