# Generated by Django 4.1.5 on 2023-02-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productreview_product_alter_productphoto_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]