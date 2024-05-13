# Generated by Django 4.2.13 on 2024-05-13 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency')),
            ],
        ),
    ]
