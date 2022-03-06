# Generated by Django 4.0.2 on 2022-02-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0019_eventrequest_events_even_type_id_16c464_idx"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="eventrequest",
            name="events_even_type_id_16c464_idx",
        ),
        migrations.AddIndex(
            model_name="eventrequest",
            index=models.Index(
                fields=["requested_by", "associated_topic"],
                name="events_even_request_beb3ea_idx",
            ),
        ),
    ]
