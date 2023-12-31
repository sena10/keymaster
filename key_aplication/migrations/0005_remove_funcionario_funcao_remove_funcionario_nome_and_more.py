# Generated by Django 4.2.1 on 2023-05-28 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('key_aplication', '0004_rename_user_funcionario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='chave',
            name='identificador',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chave',
            name='disponibilidade',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='chave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='key_aplication.chave'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data_retirada',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='key_aplication.funcionario'),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='key_aplication.chave')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='key_aplication.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='key_aplication.funcionario')),
            ],
        ),
    ]
