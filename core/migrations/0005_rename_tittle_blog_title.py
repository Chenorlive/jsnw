# Generated by Django 5.0.1 on 2024-04-30 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_question_is_suggestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tittle',
            new_name='title',
        ),
    ]