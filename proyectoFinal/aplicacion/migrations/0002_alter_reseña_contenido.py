# Generated by Django 4.2.3 on 2023-09-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseña',
            name='contenido',
            field=models.TextField(),
        ),
    ]
