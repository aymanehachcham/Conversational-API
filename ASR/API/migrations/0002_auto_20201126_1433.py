# Generated by Django 3.1.3 on 2020-11-26 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asrtext',
            old_name='text_content',
            new_name='Output',
        ),
    ]
