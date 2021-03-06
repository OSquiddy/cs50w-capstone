# Generated by Django 3.1.7 on 2021-10-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emrsystem', '0033_auto_20211016_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasthistory',
            name='cardiovascular_disease',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pasthistory',
            name='chronic_kidney_disease',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pasthistory',
            name='heart_disease',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pasthistory',
            name='hypothyroidism',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pasthistory',
            name='t2dm',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
