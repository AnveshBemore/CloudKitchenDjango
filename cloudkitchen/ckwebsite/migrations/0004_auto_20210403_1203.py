# Generated by Django 3.1.7 on 2021-04-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckwebsite', '0003_auto_20210403_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='numofprod',
            field=models.IntegerField(default=0),
        ),
    ]
