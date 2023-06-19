# Generated by Django 4.2.1 on 2023-05-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confignumbercards',
            name='Difficult',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='confignumbercards',
            name='Easy',
            field=models.PositiveSmallIntegerField(default=25),
        ),
        migrations.AddField(
            model_name='confignumbercards',
            name='Medium',
            field=models.PositiveSmallIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='configtimebonus',
            name='Difficult',
            field=models.PositiveSmallIntegerField(default=720),
        ),
        migrations.AddField(
            model_name='configtimebonus',
            name='Easy',
            field=models.PositiveSmallIntegerField(default=180),
        ),
        migrations.AddField(
            model_name='configtimebonus',
            name='Medium',
            field=models.PositiveSmallIntegerField(default=360),
        ),
    ]
