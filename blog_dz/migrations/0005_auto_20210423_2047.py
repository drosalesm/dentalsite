# Generated by Django 3.1.7 on 2021-04-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_dz', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telefono',
            field=models.IntegerField(verbose_name='Numero de telefono'),
        ),
    ]
