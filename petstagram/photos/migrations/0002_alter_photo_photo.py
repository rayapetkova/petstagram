# Generated by Django 4.2.4 on 2023-09-04 13:50

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.photos.models.validate_files_size]),
        ),
    ]