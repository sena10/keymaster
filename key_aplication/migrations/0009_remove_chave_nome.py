# Generated by Django 4.2.1 on 2023-05-29 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('key_aplication', '0008_funcionario_cpf_funcionario_telefone_sala_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chave',
            name='nome',
        ),
    ]