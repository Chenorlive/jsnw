# Generated by Django 5.0.1 on 2024-04-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_fqa',
            field=models.BooleanField(default=False),
        ),
    ]
