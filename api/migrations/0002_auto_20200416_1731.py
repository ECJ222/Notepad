# Generated by Django 3.0.5 on 2020-04-16 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notepad',
            old_name='user',
            new_name='username',
        ),
    ]
