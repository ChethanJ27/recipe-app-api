# Generated by Django 4.0.8 on 2023-02-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_usermodel_groups_usermodel_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]