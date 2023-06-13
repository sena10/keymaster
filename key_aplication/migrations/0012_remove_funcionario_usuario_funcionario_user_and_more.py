# Generated by Django 4.2.1 on 2023-06-13 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('key_aplication', '0011_alter_funcionario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguelchave',
            name='chave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alugueis', to='key_aplication.chave'),
        ),
    ]