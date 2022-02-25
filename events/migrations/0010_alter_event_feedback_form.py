# Generated by Django 4.0.2 on 2022-02-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0009_alter_event_feedback_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="feedback_form",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="events.feedbackform",
            ),
        ),
    ]