# Generated by Django 4.0.4 on 2022-06-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_material_error_model_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material_error_model',
            name='date',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
    ]