# Generated by Django 2.0.1 on 2018-03-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_goal', models.CharField(max_length=40)),
                ('complete_goal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Grat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_grat', models.CharField(max_length=80)),
                ('complete_grat', models.BooleanField(default=False)),
            ],
        ),
    ]
