# Generated by Django 3.1.2 on 2020-12-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201119_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
