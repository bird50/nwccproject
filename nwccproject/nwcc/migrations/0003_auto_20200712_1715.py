# Generated by Django 2.2.13 on 2020-07-12 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nwcc', '0002_ministry_establish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name': 'หน่วยงานระดับกรม', 'verbose_name_plural': 'หน่วยงานระดับกรม'},
        ),
        migrations.AlterModelOptions(
            name='ministry',
            options={'verbose_name': 'หน่วยงานระดับกระดับกระทรวง', 'verbose_name_plural': 'หน่วยงานระดับกระทรวง'},
        ),
    ]