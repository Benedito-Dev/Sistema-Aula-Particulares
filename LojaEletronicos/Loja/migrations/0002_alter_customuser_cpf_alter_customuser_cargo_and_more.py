# Generated by Django 5.1.4 on 2025-01-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='CPF',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cargo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]