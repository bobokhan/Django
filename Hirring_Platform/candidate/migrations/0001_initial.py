# Generated by Django 5.0.7 on 2024-08-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('skills', models.TextField()),
                ('resume', models.FileField(upload_to='resume/')),
                ('applied_jobs', models.ManyToManyField(blank=True, related_name='candidate', to='Hr.job')),
            ],
        ),
    ]
