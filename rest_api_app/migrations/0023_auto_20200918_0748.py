# Generated by Django 3.1 on 2020-09-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0022_auto_20200918_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_feed',
            name='upload_date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
