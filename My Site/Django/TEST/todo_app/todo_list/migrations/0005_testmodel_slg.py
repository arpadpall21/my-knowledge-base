# Generated by Django 4.1.5 on 2023-01-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_remove_testmodel_test_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='slg',
            field=models.SlugField(default='23abc-?'),
        ),
    ]
