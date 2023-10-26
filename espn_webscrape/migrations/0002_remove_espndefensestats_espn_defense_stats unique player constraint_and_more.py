# Generated by Django 4.1.2 on 2023-10-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espn_webscrape', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='espndefensestats',
            name='espn_defense_stats unique player constraint',
        ),
        migrations.RemoveConstraint(
            model_name='espnpassingstats',
            name='espn_passing_stats unique player constraint',
        ),
        migrations.RemoveConstraint(
            model_name='espnreceivingstats',
            name='espn_receiving_stats unique player constraint',
        ),
        migrations.RemoveConstraint(
            model_name='espnrushingstats',
            name='espn_rushing_stats unique player constraint',
        ),
        migrations.AddConstraint(
            model_name='espndefensestats',
            constraint=models.UniqueConstraint(fields=('player_full_name', 'pos', 'team_abrv'), name='espn_defense_stats unique player constraint'),
        ),
        migrations.AddConstraint(
            model_name='espnpassingstats',
            constraint=models.UniqueConstraint(fields=('player_full_name', 'pos', 'team_abrv'), name='espn_passing_stats unique player constraint'),
        ),
        migrations.AddConstraint(
            model_name='espnreceivingstats',
            constraint=models.UniqueConstraint(fields=('player_full_name', 'pos', 'team_abrv'), name='espn_receiving_stats unique player constraint'),
        ),
        migrations.AddConstraint(
            model_name='espnrushingstats',
            constraint=models.UniqueConstraint(fields=('player_full_name', 'pos', 'team_abrv'), name='espn_rushing_stats unique player constraint'),
        ),
    ]