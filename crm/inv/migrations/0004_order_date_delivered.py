# Generated by Django 3.0.5 on 2020-04-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_auto_20200415_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_delivered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
