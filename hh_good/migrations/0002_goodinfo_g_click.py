# Generated by Django 2.2.6 on 2020-04-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh_good', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodinfo',
            name='g_click',
            field=models.IntegerField(default=0),
        ),
    ]
