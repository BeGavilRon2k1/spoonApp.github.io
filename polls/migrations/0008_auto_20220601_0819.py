# Generated by Django 2.2.12 on 2022-06-01 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_numvalueingrediente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numvalueingrediente',
            old_name='GrasasSaturadas',
            new_name='SaturedFat',
        ),
    ]
