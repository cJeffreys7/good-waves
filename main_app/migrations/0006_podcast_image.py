# Generated by Django 3.2.7 on 2021-11-30 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211129_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='image',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
