# Generated by Django 5.1.4 on 2025-01-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='positions',
            name='behaviouranalyst',
            field=models.CharField(default='Admin', max_length=255),
            preserve_default=False,
        ),
    ]