# Generated by Django 4.0 on 2022-03-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='document',
            field=models.FileField(default=0, upload_to='static/doc'),
        ),
    ]
