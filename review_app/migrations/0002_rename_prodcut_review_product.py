# Generated by Django 4.1.2 on 2022-10-29 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='prodcut',
            new_name='product',
        ),
    ]
