# Generated by Django 4.1.5 on 2023-02-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_order_deliverer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='priority',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
