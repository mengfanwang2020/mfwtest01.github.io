# Generated by Django 2.2.25 on 2021-12-18 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20211218_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='tect',
            new_name='text',
        ),
    ]
