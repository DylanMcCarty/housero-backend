# Generated by Django 4.1.3 on 2022-12-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Housero', '0002_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='max_price',
            field=models.DecimalField(decimal_places=0, max_digits=9, null=True),
        ),
    ]
