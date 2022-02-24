# Generated by Django 4.0.2 on 2022-02-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedbackform",
            name="acceptingSubmissions",
        ),
        migrations.AddField(
            model_name="feedbackform",
            name="acceptingSubmissionsUntil",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="feedbackform",
            name="desc",
            field=models.TextField(blank=True),
        ),
    ]