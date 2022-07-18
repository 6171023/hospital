# Generated by Django 4.0.6 on 2022-07-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='generaluser',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='generaluser',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
