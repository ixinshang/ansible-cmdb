# Generated by Django 2.0.1 on 2018-07-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20180719_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager_persion',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
