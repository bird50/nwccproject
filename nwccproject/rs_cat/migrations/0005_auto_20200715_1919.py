# Generated by Django 2.2.13 on 2020-07-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs_cat', '0004_auto_20200713_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rs_cat',
            name='GroupActPrb',
            field=models.TextField(blank=True, null=True, verbose_name='กลุ่มข้อมูลตามยุทธศาสตร์ และ พรบ.'),
        ),
    ]
