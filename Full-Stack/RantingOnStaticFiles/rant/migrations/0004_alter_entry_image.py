# Generated by Django 4.1.7 on 2023-03-17 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rant', '0003_entry_desc_entry_title_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
