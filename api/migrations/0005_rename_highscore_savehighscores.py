# Generated by Django 4.1 on 2023-06-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_highscore'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HighScore',
            new_name='SaveHighScores',
        ),
    ]