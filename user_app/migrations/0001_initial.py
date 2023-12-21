# Generated by Django 5.0 on 2023-12-21 10:27

import django.contrib.auth.password_validation
import django.utils.timezone
import user_app.models
import user_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists'}, help_text='Required. Your gmail address.', max_length=254, unique=True, validators=[user_app.validators.validate_email], verbose_name='email address')),
                ('birth_date', models.DateField(default=django.utils.timezone.now, help_text='Required. Your birth date.')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', help_text='Required. Choose your gender.', max_length=1)),
                ('phone_number', models.CharField(blank=True, error_messages={'invalid': 'Please enter a valid phone', 'unique': 'A user with that phone number already exists'}, help_text='Enter phone number e.g: +998123456789', max_length=13, null=True, unique=True, validators=[user_app.validators.PhoneValidator()], verbose_name='phone number')),
                ('password', models.CharField(max_length=100, validators=[django.contrib.auth.password_validation.validate_password])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
            managers=[
                ('objects', user_app.models.BaseUserManager()),
            ],
        ),
    ]