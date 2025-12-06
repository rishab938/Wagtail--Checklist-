from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/<int:page_id>/", views.checklist_dashboard, name="checklist_dashboard"),
    path("add/<int:page_id>/", views.add_task, name="checklist_add"),
    path("approve/<int:task_id>/", views.approve_task, name="checklist_approve"),
    path("reject/<int:task_id>/", views.reject_task, name="checklist_reject"),
]
