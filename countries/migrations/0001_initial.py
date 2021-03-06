# Generated by Django 3.1.5 on 2021-06-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('wiki', models.URLField()),
                ('alpha2', models.CharField(max_length=2)),
                ('alpha3', models.CharField(max_length=3)),
                ('countrycode', models.IntegerField()),
                ('region', models.CharField(max_length=30)),
                ('subregion', models.CharField(max_length=30)),
                ('interregion', models.CharField(max_length=30)),
                ('regioncode', models.IntegerField()),
                ('subregioncode', models.IntegerField()),
                ('interregioncode', models.IntegerField()),
            ],
        ),
    ]
