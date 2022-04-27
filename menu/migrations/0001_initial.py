# Generated by Django 2.2.14 on 2021-12-22 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('typeOfMagazine', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
                ('price', models.IntegerField()),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MarketName')),
            ],
        ),
    ]