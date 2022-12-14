# Generated by Django 4.1.3 on 2022-12-07 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Housero', '0003_alter_criteria_max_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='max_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='min_price',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=9),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
