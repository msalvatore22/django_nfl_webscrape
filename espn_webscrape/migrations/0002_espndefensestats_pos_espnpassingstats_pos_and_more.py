# Generated by Django 4.1.2 on 2022-11-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espn_webscrape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='espndefensestats',
            name='pos',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='espnpassingstats',
            name='pos',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='espnreceivingstats',
            name='pos',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='espnrushingstats',
            name='pos',
            field=models.CharField(max_length=4, null=True),
        ),
    ]