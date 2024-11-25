# Generated by Django 5.1.3 on 2024-11-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('custo_por_hectare', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
