# Generated by Django 4.0.6 on 2022-07-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other'), (3, 'Do not wish to answer')])),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=512)),
                ('tel', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=64)),
                ('allergies', models.ManyToManyField(to='landing.allergy')),
            ],
        ),
    ]
