# Generated by Django 3.1 on 2020-09-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0024_auto_20200918_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_feed',
            name='ad_genre',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='module_feed',
            name='ad_links',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='module_feed',
            name='ad_title',
            field=models.TextField(max_length=255, null=True),
        ),
    ]