# Generated by Django 5.1.4 on 2025-01-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quant', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
    ]
