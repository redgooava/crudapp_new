# Generated by Django 2.2 on 2022-02-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatable',
            name='cell_48',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
