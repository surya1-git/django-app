# Generated by Django 4.2 on 2023-04-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('objects_detected', models.CharField(max_length=200)),
                ('timestamp', models.CharField(max_length=200)),
            ],
        ),
    ]