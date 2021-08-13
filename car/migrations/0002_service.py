# Generated by Django 3.2.6 on 2021-08-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('company', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
            ],
        ),
    ]
