# Generated by Django 4.1.7 on 2023-03-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rant', '0004_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ppic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
