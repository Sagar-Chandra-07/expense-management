# Generated by Django 3.2.10 on 2023-04-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_tile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('issue', models.CharField(max_length=100)),
            ],
        ),
    ]
