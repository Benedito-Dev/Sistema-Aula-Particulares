# Generated by Django 5.1.4 on 2025-01-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loja', '0002_produto_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]
