# Generated by Django 3.1.7 on 2021-04-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckwebsite', '0002_auto_20210428_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='uname',
            new_name='name',
        ),
    ]