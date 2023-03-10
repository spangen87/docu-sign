# Generated by Django 3.2 on 2023-02-21 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0013_auto_20230216_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstallationDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=24, verbose_name='Automatik serie-/batch-nr')),
                ('date_in_use', models.DateField(verbose_name='Datum för driftsättning')),
                ('installed_by', models.CharField(max_length=54, verbose_name='Installerad av företag')),
                ('technician', models.CharField(max_length=54, verbose_name='v/tekniker')),
                ('door_type', models.CharField(choices=[('1-flyg', '1-flyg'), ('2-flyg', '2-flyg')], max_length=6, verbose_name='Dörrparti')),
                ('weight', models.CharField(max_length=24, verbose_name='Antagen vikt per dörrblad')),
                ('width', models.CharField(max_length=24, verbose_name='Total bredd')),
                ('kind_of_door', models.CharField(choices=[('WOOD', 'Trä'), ('STEEL', 'Stål'), ('ALUMINIUM', 'Aluminium'), ('PROFILE', 'Profil'), ('GLASS', 'Glas')], max_length=9, verbose_name='Dörrtyp')),
                ('program_selector_internal', models.BooleanField(verbose_name='Programväljare internt')),
                ('program_selector_internal_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('program_selector_external', models.BooleanField(verbose_name='Programväljare externt')),
                ('program_selector_external_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('electromechanical_lock_internal', models.BooleanField(verbose_name='Elektromekaniskt lås internt')),
                ('electromechanical_lock_internal_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('electromechanical_lock_external', models.BooleanField(verbose_name='Elektromekaniskt lås externt')),
                ('electromechanical_lock_external_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('mechanical_micro_switch', models.BooleanField(verbose_name='Mekaniskt lås med mikrobrytare')),
                ('mechanical_micro_switch_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('impulse_generator', models.BooleanField(verbose_name='Impulsgivare')),
                ('impulse_generator_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('sensors', models.BooleanField(verbose_name='Sensorer')),
                ('sensors_notes', models.CharField(max_length=200, verbose_name='Kommentar')),
                ('door_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='door_automation_forms.riskanalysis')),
                ('object_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='door_automation_forms.object')),
            ],
            options={
                'verbose_name': 'Installationsbeskrivning',
                'verbose_name_plural': 'Installationsbeskrivningar',
            },
        ),
    ]
