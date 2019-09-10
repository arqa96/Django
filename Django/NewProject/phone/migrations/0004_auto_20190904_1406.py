# Generated by Django 2.2.4 on 2019-09-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_auto_20190903_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='metro',
            field=models.CharField(choices=[('Адмиралтейская', 'Адмиралтейская'), ('Новочеркасская', 'Новочеркасская'), ('Площадь Восстания', 'Площадь Восстания')], max_length=20, verbose_name='станция метро'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(choices=[('Apple', 'Apple'), ('Samsung', 'Samsung'), ('Xiaomi', 'Xiaomi'), ('LG', 'LG')], max_length=20, verbose_name='телефон'),
        ),
    ]