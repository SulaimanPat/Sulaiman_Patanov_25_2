# Generated by Django 4.1.7 on 2023-03-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_hashtag_product_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='title',
            field=models.CharField(max_length=55),
        ),
    ]