# Generated by Django 4.1.7 on 2023-03-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rant', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='desc',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]