# Generated by Django 4.2 on 2023-09-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_foodaction_remove_foodhistory_food_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodhistory',
            name='eaten',
            field=models.CharField(choices=[('thrown_away', 'Throw it away'), ('upcycled', 'Upcycled')], max_length=20, null=True),
        ),
    ]
