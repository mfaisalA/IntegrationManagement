# Generated by Django 2.1.2 on 2020-02-02 06:56

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facultymember',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='facultymember',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='facultymember',
            name='privileges',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('lec', 'Lecurer'), ('crs', 'Course Head')], max_length=3),
        ),
    ]