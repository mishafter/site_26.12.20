# Generated by Django 3.1.4 on 2020-12-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20201224_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='cekh',
            name='filial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.filial', verbose_name='name'),
        ),
    ]
