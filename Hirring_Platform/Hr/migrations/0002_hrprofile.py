# Generated by Django 5.0.7 on 2024-08-29 21:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hr', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HRProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('position_title', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hr_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
