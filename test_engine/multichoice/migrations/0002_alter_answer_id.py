# Generated by Django 5.1.1 on 2024-09-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multichoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
