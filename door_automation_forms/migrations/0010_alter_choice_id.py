# Generated by Django 3.2 on 2023-02-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_automation_forms', '0009_alter_choice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
