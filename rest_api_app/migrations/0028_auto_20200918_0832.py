# Generated by Django 3.1 on 2020-09-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0027_auto_20200918_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_feed',
            name='total_videos',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
