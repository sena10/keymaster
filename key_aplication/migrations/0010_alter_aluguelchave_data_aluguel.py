# Generated by Django 4.2.1 on 2023-05-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_aplication', '0009_remove_chave_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguelchave',
            name='data_aluguel',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
