# Generated by Django 5.0 on 2023-12-22 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestmodel',
            options={'ordering': ('publish_date',), 'verbose_name': 'contest', 'verbose_name_plural': 'contests'},
        ),
    ]
