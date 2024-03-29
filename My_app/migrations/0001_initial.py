# Generated by Django 4.2.9 on 2024-02-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.CharField(max_length=20, unique=True)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('class_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
