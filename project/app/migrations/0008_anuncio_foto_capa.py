# Generated by Django 3.0.6 on 2020-06-22 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_anuncio_foto_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='foto_capa',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='imagens'),
            preserve_default=False,
        ),
    ]
