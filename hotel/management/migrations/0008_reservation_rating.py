# Generated by Django 4.2.11 on 2024-05-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_hotels_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
