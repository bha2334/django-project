# Generated by Django 3.0.8 on 2020-10-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0003_sfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfile',
            name='pdf',
            field=models.FileField(upload_to='desktop/pdf'),
        ),
    ]
