# Generated by Django 3.1.7 on 2021-04-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_dz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
