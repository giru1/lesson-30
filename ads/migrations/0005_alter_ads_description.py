# Generated by Django 4.0.5 on 2022-09-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_rename_author_id_ads_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
