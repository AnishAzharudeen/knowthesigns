# Generated by Django 4.2.18 on 2025-01-17 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_line_address', models.CharField(blank=True, max_length=100, null=True)),
                ('second_line_address', models.CharField(blank=True, max_length=100, null=True)),
                ('town_city', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('person_of_trust', models.CharField(blank=True, max_length=50, null=True)),
                ('person_of_trust_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('image_video_url', models.URLField(blank=True, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report')),
            ],
        ),
    ]