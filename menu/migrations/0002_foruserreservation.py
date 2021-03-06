# Generated by Django 3.2.10 on 2022-05-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForUserReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('full_adress', models.CharField(max_length=400)),
                ('phone_num', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('summa', models.CharField(max_length=100)),
                ('products', models.JSONField()),
            ],
        ),
    ]
