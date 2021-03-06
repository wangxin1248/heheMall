# Generated by Django 2.2.6 on 2020-05-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hh_good', '0003_goodinfo_g_unit'),
        ('hh_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hh_good.GoodInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hh_user.UserInfo')),
            ],
        ),
    ]
