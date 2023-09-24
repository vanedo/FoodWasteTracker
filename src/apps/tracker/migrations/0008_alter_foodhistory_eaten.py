# Generated by Django 4.2 on 2023-09-24 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_remove_foodhistory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodhistory',
            name='eaten',
            field=models.CharField(choices=[('thrown_away', 'Throw it away'), ('upcycled', 'Upcycle')], max_length=20, null=True, verbose_name='Action'),
        ),
    ]