# Generated by Django 4.1.1 on 2022-10-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0008_remove_agent_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_secteur',
            field=models.IntegerField(null=True, verbose_name='agent secteur'),
        ),
        migrations.AddField(
            model_name='agent',
            name='secteur_primaire',
            field=models.CharField(max_length=300, null=True, verbose_name='secteur primaire'),
        ),
        migrations.AddField(
            model_name='agent',
            name='secteur_secondaire',
            field=models.CharField(max_length=300, null=True, verbose_name='secteur secondaire'),
        ),
    ]