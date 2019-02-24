# Generated by Django 2.1.7 on 2019-02-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametext', models.CharField(max_length=500)),
                ('descriptiontext', models.CharField(max_length=1500)),
                ('organization_id', models.BigIntegerField()),
                ('online_event', models.CharField(max_length=500)),
                ('startutc', models.DateTimeField(verbose_name='startutc')),
                ('endutc', models.DateTimeField(verbose_name='endutc')),
                ('listed', models.BooleanField()),
                ('is_free', models.BooleanField()),
                ('url', models.CharField(max_length=500)),
                ('resource_uri', models.CharField(max_length=500)),
            ],
        ),
    ]