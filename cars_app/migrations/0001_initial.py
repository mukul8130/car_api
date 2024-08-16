# Generated by Django 4.1.7 on 2024-08-07 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(upload_to='')),
                ('car_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('car_title', models.CharField(max_length=100)),
                ('car_price', models.IntegerField()),
                ('car_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_category.category_table')),
            ],
        ),
    ]
