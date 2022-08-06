# Generated by Django 3.2 on 2022-08-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_account_pin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Место работы', 'verbose_name_plural': 'Места работы'},
        ),
        migrations.AlterField(
            model_name='work',
            name='postalZip',
            field=models.CharField(max_length=20, verbose_name='Почтовый индекс'),
        ),
    ]
