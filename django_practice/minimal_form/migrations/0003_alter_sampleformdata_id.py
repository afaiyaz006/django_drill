# Generated by Django 4.0.1 on 2022-01-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimal_form', '0002_alter_sampleformdata_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleformdata',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
