# Generated by Django 2.1.4 on 2018-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_news', '0006_auto_20181217_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url_to_image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
