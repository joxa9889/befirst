# Generated by Django 5.0 on 2023-12-18 16:36

import contest_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title of the contest.', max_length=150)),
                ('slug', models.SlugField(blank=True, help_text="a slug that appears in the url. If not provided, 'title' will be used instead", null=True, unique=True)),
                ('description', models.TextField(blank=True, help_text='Description of the contest.', null=True)),
                ('banner_image', models.ImageField(help_text='Required. A banner image of the contest', upload_to=contest_app.models.ContestModel.user_directory_path)),
                ('start_date', models.DateTimeField(help_text='Required. The start date of the contest.')),
                ('end_date', models.DateTimeField(help_text='Required. The end date of the contest.')),
                ('publish_date', models.DateTimeField(help_text='Required. The date when results will be published.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contest',
                'verbose_name_plural': 'contests',
                'db_table': 'contest',
            },
        ),
        migrations.CreateModel(
            name='ExpertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(blank=True, help_text='Some details about the expert.', null=True)),
            ],
            options={
                'verbose_name': 'expert',
                'verbose_name_plural': 'experts',
                'db_table': 'expert',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, help_text='Your profile picture.', null=True, upload_to=contest_app.models.ProfileModel.user_directory_path)),
                ('address', models.TextField(blank=True, help_text='Enter your address here. e.g: 45/9 Sergeli 7, Tashkent Shahar', null=True)),
                ('news_agreement', models.BooleanField(default=True, help_text='Do you want to receive e-mails from us? e.g: information about new contests')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required. The name of the region.', max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='ScoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, help_text='How would you assess the work on the scale from 1 to 10?')),
            ],
            options={
                'verbose_name': 'score',
                'verbose_name_plural': 'scores',
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of a work.', max_length=100)),
                ('file', models.FileField(help_text='Upload the file.', upload_to=contest_app.models.WorkModel.user_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
                'db_table': 'work',
            },
        ),
    ]
