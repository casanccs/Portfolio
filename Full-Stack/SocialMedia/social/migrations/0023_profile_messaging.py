# Generated by Django 4.1.5 on 2023-02-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0022_remove_comment_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='messaging',
            field=models.ManyToManyField(blank=True, to='social.profile'),
        ),
    ]