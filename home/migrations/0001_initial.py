# Generated by Django 3.0 on 2023-03-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('sal', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
                ('mob', models.IntegerField()),
            ],
        ),
    ]