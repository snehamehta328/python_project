# Generated by Django 3.1.7 on 2021-04-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cebsApp', '0007_auto_20210412_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='contactNum',
            field=models.IntegerField(default=32973874),
            preserve_default=False,
        ),
    ]
