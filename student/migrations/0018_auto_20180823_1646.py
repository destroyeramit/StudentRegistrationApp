# Generated by Django 2.0.6 on 2018-08-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20180823_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_form1',
            name='Nationality',
            field=models.CharField(choices=[('India', 'India'), ('Foreign', 'Foreign')], max_length=7),
        ),
    ]