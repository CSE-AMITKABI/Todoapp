# Generated by Django 4.0.6 on 2022-07-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0002_rename_todolists_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
    ]
