# Generated by Django 3.1.7 on 2021-09-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emrsystem', '0010_visit_visit_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='general',
            new_name='others',
        ),
        migrations.AddField(
            model_name='examination',
            name='clubbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examination',
            name='icterus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examination',
            name='koilonychia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examination',
            name='lymphadenopathy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examination',
            name='pallor',
            field=models.BooleanField(default=False),
        ),
    ]
