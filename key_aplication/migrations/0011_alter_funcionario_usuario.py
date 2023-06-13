# Generated by Django 4.2.1 on 2023-05-29 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('key_aplication', '0010_alter_aluguelchave_data_aluguel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
        ),
    ]