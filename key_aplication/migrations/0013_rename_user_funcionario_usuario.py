# Generated by Django 4.2.1 on 2023-06-13 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('key_aplication', '0012_remove_funcionario_usuario_funcionario_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='user',
            new_name='usuario',
        ),
    ]
