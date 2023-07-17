# Generated by Django 4.1.6 on 2023-02-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=16)),
                ('feedback', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
