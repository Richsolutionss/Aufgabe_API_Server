# Generated by Django 3.0.6 on 2020-05-04 13:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='Preis',
            new_name='preis',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='Produkt_url',
            new_name='produkt_url',
        ),
        migrations.AddField(
            model_name='server',
            name='hersteller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend2.Hersteller'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='lager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend2.Lager'),
            preserve_default=False,
        ),
    ]
