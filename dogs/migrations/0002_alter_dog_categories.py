# Generated by Django 4.2.7 on 2023-11-30 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='categories',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='dogs.categories', verbose_name='Порода'),
        ),
    ]
