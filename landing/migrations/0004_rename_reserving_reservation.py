# Generated by Django 4.0.6 on 2022-07-18 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_reserving'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserving',
            new_name='Reservation',
        ),
    ]
