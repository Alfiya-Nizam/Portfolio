# Generated by Django 4.0.4 on 2024-04-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortApp', '0003_experiencedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sdate', models.DateField()),
                ('edate', models.DateField()),
                ('university', models.CharField(max_length=100)),
                ('mark', models.CharField(max_length=100)),
            ],
        ),
    ]
