# Generated by Django 3.2 on 2023-03-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0017_auto_20230227_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskanalysis',
            name='notes',
        ),
        migrations.AddField(
            model_name='riskanalysis',
            name='A_note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anmärkningar'),
        ),
        migrations.AddField(
            model_name='riskanalysis',
            name='B_note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anmärkningar'),
        ),
        migrations.AddField(
            model_name='riskanalysis',
            name='C_note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anmärkningar'),
        ),
        migrations.AddField(
            model_name='riskanalysis',
            name='D_note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anmärkningar'),
        ),
        migrations.AddField(
            model_name='riskanalysis',
            name='E_note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anmärkningar'),
        ),
    ]
