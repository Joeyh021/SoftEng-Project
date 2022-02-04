import uuid

from django.db import models


class Event:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    startTime = models.DateTimeField()
    location = models.TextField()
    duration = models.IntegerField()
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    feedback_form = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)


class EventType:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    max_members = models.IntegerField()
    min_members = models.IntegerField()


class EventAttendee:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_index=True)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        indexes = [models.Index(fields=["event", "attendee"])]


class EventRequest:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    associated_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class FeedbackForm:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    acceptingSubmissions = models.BooleanField(default=true)


class Questions:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    data = models.JSONField()
    form = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)
    order = models.IntegerField()
    required = models.BooleanField()


class QuestionType:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type_data = models.JSONField()


class Answer:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    associated_question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    associated_submission = models.ForeignKey(
        FeedbackSubmission, on_delete=models.CASCADE
    )
    data = models.CharField(max_length=200)


class FeedbackSubmission:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)