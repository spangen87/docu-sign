# Generated by Django 3.2 on 2023-02-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0012_auto_20230216_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskanalysis',
            name='A',
            field=models.CharField(blank=True, max_length=84, null=True, verbose_name='A. Klämrisk*'),
        ),
        migrations.AlterField(
            model_name='riskanalysis',
            name='B',
            field=models.CharField(blank=True, max_length=84, null=True, verbose_name='B. Klämrisk*'),
        ),
        migrations.AlterField(
            model_name='riskanalysis',
            name='C',
            field=models.CharField(blank=True, max_length=84, null=True, verbose_name='C. Klämrisk'),
        ),
        migrations.AlterField(
            model_name='riskanalysis',
            name='D',
            field=models.CharField(blank=True, max_length=84, null=True, verbose_name='D. Klämrisk'),
        ),
        migrations.AlterField(
            model_name='riskanalysis',
            name='E',
            field=models.CharField(blank=True, max_length=84, null=True, verbose_name='E. Klämrisk'),
        ),
    ]