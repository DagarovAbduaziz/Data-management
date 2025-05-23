# Generated by Django 4.2.2 on 2025-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_patient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='contact',
            new_name='occupation',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='role',
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
