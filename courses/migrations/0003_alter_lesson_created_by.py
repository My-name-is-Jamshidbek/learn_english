# Generated by Django 5.0.4 on 2024-04-30 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_staffprofile_country_and_more'),
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='accounts.staffprofile'),
        ),
    ]
