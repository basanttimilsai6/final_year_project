# Generated by Django 4.0.2 on 2022-03-03 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0003_note_category_alter_material_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='image',
            field=models.FileField(upload_to='static/images'),
        ),
    ]
