# Generated by Django 3.2 on 2023-02-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0016_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='installation_changed_notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rapport/fel/ska utföras'),
        ),
        migrations.AlterField(
            model_name='service',
            name='other_notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rapport/fel/ska utföras'),
        ),
        migrations.AlterField(
            model_name='service',
            name='periodic_control_notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rapport/fel/ska utföras'),
        ),
        migrations.AlterField(
            model_name='service',
            name='repair_ordered_notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rapport/fel/ska utföras'),
        ),
    ]
