# Generated by Django 2.0.6 on 2018-08-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Middel_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('Nationality', models.CharField(choices=[('I', 'India'), ('N', 'Foreign')], max_length=5)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'female'), ('O', 'other')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student_form2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mother_name', models.CharField(max_length=100)),
                ('Father_name', models.CharField(max_length=100)),
                ('tenth_marks', models.CharField(max_length=3)),
                ('Twelfth_result', models.CharField(choices=[('A', 'Awaited'), ('P', 'Passed')], max_length=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Twelfth_marks', models.CharField(blank=True, max_length=3)),
                ('Subject1_marks', models.CharField(blank=True, max_length=3)),
                ('Subject2_marks', models.CharField(blank=True, max_length=3)),
                ('Subject3_marks', models.CharField(blank=True, max_length=3)),
                ('Subject4_marks', models.CharField(blank=True, max_length=3)),
            ],
        ),
    ]
