# Generated by Django 3.1 on 2020-09-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0014_auto_20200918_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_feed',
            name='channel_name',
            field=models.CharField(max_length=510, null=True),
        ),
        migrations.AlterField(
            model_name='module_feed',
            name='creation_date',
            field=models.CharField(max_length=510, null=True),
        ),
        migrations.AlterField(
            model_name='module_feed',
            name='upload_date',
            field=models.CharField(max_length=510, null=True),
        ),
    ]