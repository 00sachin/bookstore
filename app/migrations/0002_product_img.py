# Generated by Django 4.0.4 on 2022-08-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='pics'),
        ),
    ]