# Generated by Django 5.1.3 on 2024-11-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previsoes', '0002_areaplantada_valorproducao_delete_cultivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosAgricolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('regiao', models.CharField(blank=True, max_length=100, null=True)),
                ('cultura', models.CharField(max_length=100)),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AreaPlantada',
        ),
        migrations.DeleteModel(
            name='ValorProducao',
        ),
    ]
