# Generated by Django 4.1.1 on 2022-10-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0009_agent_agent_secteur_agent_secteur_primaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='telephone',
            field=models.CharField(max_length=40, null=True, verbose_name='telephone'),
        ),
    ]