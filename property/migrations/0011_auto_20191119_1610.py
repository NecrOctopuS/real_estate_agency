# Generated by Django 2.2.4 on 2019-11-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20191119_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_phone_pure',
            new_name='phone_pure',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_link',
            field=models.ManyToManyField(blank=True, related_name='owner_flats', to='property.Owner', verbose_name='Владелец'),
        ),
    ]
