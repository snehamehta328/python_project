# Generated by Django 3.1.7 on 2021-04-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID',default=1)),
                ('uname', models.CharField(max_length=100)),
                ('uemail', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('contactNum', models.IntegerField()),
            ],
            options={
                'db_table': 'RegForm',
            },
        ),
    ]