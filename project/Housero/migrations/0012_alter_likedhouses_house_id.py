# Generated by Django 4.1.3 on 2022-12-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Housero', '0011_alter_likedhouses_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedhouses',
            name='house_id',
            field=models.IntegerField(null=True),
        ),
    ]
