# Generated by Django 4.1.7 on 2023-03-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rant', '0005_alter_profile_ppic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='entry',
            name='image2',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image3',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image4',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image5',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
