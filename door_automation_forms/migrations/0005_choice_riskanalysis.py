# Generated by Django 3.2 on 2023-02-14 15:15

from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0004_auto_20230209_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RiskAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_id', models.CharField(max_length=14, verbose_name='Dörr-ID/platsbeskrivning')),
                ('risk', models.CharField(choices=[('LOW', 'Låg risk'), ('HIGH', 'Hög risk')], max_length=4, verbose_name='Risknivå')),
                ('automatic_model', models.CharField(max_length=54, verbose_name='Automatisk modell')),
                ('notes', models.TextField(help_text='Ange anmärkningar. Börja med bokstaven följt av notering. Ny anmärkning på ny rad.', max_length=1000, verbose_name='Anmärkningar')),
                ('date', models.DateField()),
                ('supplier', models.CharField(max_length=54, verbose_name='Leverantör')),
                ('done_by', models.CharField(max_length=54, verbose_name='Utfört av')),
                ('signature', jsignature.fields.JSignatureField()),
                ('A', models.ManyToManyField(related_name='a_choices', to='door_automation_forms.Choice')),
                ('B', models.ManyToManyField(related_name='b_choices', to='door_automation_forms.Choice')),
                ('C', models.ManyToManyField(related_name='c_choices', to='door_automation_forms.Choice')),
                ('D', models.ManyToManyField(related_name='d_choices', to='door_automation_forms.Choice')),
                ('E', models.ManyToManyField(related_name='e_choices', to='door_automation_forms.Choice')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='door_automation_forms.object')),
            ],
            options={
                'verbose_name': 'Risk analys',
                'verbose_name_plural': 'Risk analyser',
            },
        ),
    ]