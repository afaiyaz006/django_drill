# Generated by Django 4.0.1 on 2022-01-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch_no',
            field=models.IntegerField(),
        ),
    ]
