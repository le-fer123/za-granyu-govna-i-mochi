# Generated by Django 5.1.7 on 2025-03-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.SlugField(blank=True, unique=True)),
                ('content', models.FileField(upload_to='')),
            ],
        ),
    ]
