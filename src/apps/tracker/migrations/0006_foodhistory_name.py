# Generated by Django 4.2 on 2023-09-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_foodhistory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodhistory',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
