# Generated by Django 3.2.16 on 2024-12-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100)),
            ],
        ),
    ]