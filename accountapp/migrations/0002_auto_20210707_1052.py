# Generated by Django 3.2.4 on 2021-07-07 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoinMoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=225)),
            ],
        ),
        migrations.DeleteModel(
            name='BonBon',
        ),
    ]
