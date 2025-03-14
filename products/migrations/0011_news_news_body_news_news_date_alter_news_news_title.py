# Generated by Django 5.1.6 on 2025-03-10 18:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=100),
        ),
    ]
