# Generated by Django 4.2.1 on 2023-06-13 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('key_aplication', '0014_rename_usuario_funcionario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='user',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
