# Generated by Django 3.2.7 on 2021-11-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_podcast_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]