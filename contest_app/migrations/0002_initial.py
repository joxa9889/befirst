# Generated by Django 4.2.8 on 2023-12-30 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(help_text='Choose a user.', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expertmodel',
            name='user',
            field=models.OneToOneField(help_text='Choose an expert.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expert', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contestmodel',
            name='experts',
            field=models.ManyToManyField(help_text='Required. Select experts for the contest.', related_name='contests', to='contest_app.expertmodel'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='comment_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest_app.profilemodel'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='comment_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest_app.contestmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='scoremodel',
            unique_together={('expert', 'work')},
        ),
    ]
