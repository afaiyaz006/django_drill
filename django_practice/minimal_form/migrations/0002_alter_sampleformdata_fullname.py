# Generated by Django 4.0.1 on 2022-01-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimal_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleformdata',
            name='fullname',
            field=models.CharField(max_length=30),
        ),
    ]
