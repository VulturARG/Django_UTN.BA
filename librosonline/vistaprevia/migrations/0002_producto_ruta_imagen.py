# Generated by Django 2.2 on 2020-12-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ruta_imagen',
            field=models.FileField(blank=True, default='defecto/defecto.png', null=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]