# Generated manually — all existing visits already have an assigned doctor.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emrsystem', '0038_nullable_vitals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='assigned_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emrsystem.doctor'),
        ),
    ]
