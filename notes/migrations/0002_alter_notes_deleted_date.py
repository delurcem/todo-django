# Generated by Django 4.0.5 on 2022-06-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
