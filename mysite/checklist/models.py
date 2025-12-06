from django.db import models
from wagtail.models import Page


class ChecklistTask(models.Model):
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name="checklist_tasks"
    )
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
