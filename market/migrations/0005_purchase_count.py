# Generated by Django 3.2.16 on 2023-04-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]