# Generated by Django 5.0.3 on 2024-04-21 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_equipment_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviceMaker',
            new_name='DeviceWarranty',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='devicemaker',
            new_name='devicewarranty',
        ),
    ]
