# Generated by Django 2.0.6 on 2018-08-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20180823_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prob_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Subject', models.CharField(blank=True, max_length=200)),
                ('Description', models.CharField(blank=True, max_length=500)),
                ('Error_number', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
