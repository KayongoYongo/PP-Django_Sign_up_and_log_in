# Generated by Django 4.2.9 on 2024-02-14 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hashed_password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('session_id', models.CharField(blank=True, max_length=100, null=True)),
                ('reset_token', models.CharField(blank=True, max_length=100, null=True)),
                ('daate_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
