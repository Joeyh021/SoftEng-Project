# Generated by Django 4.0.2 on 2022-03-08 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_merge_20220228_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentormentee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentormentee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
