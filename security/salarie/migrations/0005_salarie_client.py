# Generated by Django 4.1.1 on 2022-09-20 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_remove_client_passeur_remove_client_salarie_and_more'),
        ('salarie', '0004_remove_salarie_actif'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarie',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_pro_rattache', to='client.client'),
        ),
    ]