# Generated by Django 4.2.1 on 2023-05-25 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('disponibilidade', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_retirada', models.DateTimeField(auto_now_add=True)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='key_aplication.chave')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('funcao', models.CharField(max_length=25)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chave',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='key_aplication.sala'),
        ),
    ]
