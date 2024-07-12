# Generated by Django 5.0.7 on 2024-07-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('sex', models.FloatField()),
                ('bmi', models.FloatField()),
                ('childrens', models.FloatField()),
                ('smoker', models.FloatField()),
                ('region', models.FloatField()),
                ('expenses', models.FloatField()),
            ],
        ),
    ]
