# Generated by Django 3.1.4 on 2020-12-24 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_cekh_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cekh',
            name='filial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.region', verbose_name='name'),
        ),
    ]
