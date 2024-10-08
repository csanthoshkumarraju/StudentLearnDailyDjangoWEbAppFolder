# Generated by Django 5.1.1 on 2024-09-19 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='studentdailymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_plan', models.TextField(null=True)),
                ('daily_status', models.CharField(default='To do', max_length=500, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dailyplans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
