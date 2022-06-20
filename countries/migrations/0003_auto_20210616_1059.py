# Generated by Django 3.1.5 on 2021-06-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20210616_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='image',
        ),
        migrations.RemoveField(
            model_name='country',
            name='wiki',
        ),
        migrations.AlterField(
            model_name='country',
            name='interregion',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='country',
            name='interregioncode',
            field=models.IntegerField(blank=True),
        ),
    ]
