# Generated by Django 4.0.4 on 2022-06-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_nosotros_delete_entregable'),
    ]

    operations = [
        migrations.AddField(
            model_name='nosotros',
            name='url',
            field=models.CharField(default='url', max_length=100),
            preserve_default=False,
        ),
    ]
