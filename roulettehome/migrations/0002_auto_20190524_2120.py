# Generated by Django 2.2 on 2019-05-24 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roulettehome', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChineseFood',
        ),
        migrations.DeleteModel(
            name='Dessert',
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='FastFood',
        ),
        migrations.DeleteModel(
            name='JapaneseFood',
        ),
        migrations.DeleteModel(
            name='KoreanFood',
        ),
        migrations.DeleteModel(
            name='WesternFood',
        ),
    ]