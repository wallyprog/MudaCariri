# Generated by Django 3.0.6 on 2020-06-22 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_anuncio_foto_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='foto_capa',
        ),
    ]
