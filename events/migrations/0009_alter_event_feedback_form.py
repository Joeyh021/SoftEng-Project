# Generated by Django 4.0.2 on 2022-02-24 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_defaultfeedbackforms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='feedback_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.feedbackform'),
        ),
    ]
