# Generated by Django 2.2.2 on 2019-10-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
