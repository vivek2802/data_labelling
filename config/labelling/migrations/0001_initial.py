# Generated by Django 2.2.6 on 2019-10-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=255)),
                ('is_labelled', models.BooleanField(default=False)),
                ('label', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]