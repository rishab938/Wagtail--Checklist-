from django.shortcuts import render, redirect
from .models import ChecklistTask
from wagtail.models import Page


def checklist_dashboard(request, page_id):
    page = Page.objects.get(id=page_id)
    tasks = ChecklistTask.objects.filter(page=page)

    return render(request, "checklist/dashboard.html", {
        "page": page,
        "tasks": tasks,
    })


def add_task(request, page_id):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            ChecklistTask.objects.create(page_id=page_id, title=title)
    return redirect("checklist_dashboard", page_id=page_id)


def approve_task(request, task_id):
    task = ChecklistTask.objects.get(id=task_id)
    task.status = "approved"
    task.save()
    return redirect("checklist_dashboard", page_id=task.page_id)


def reject_task(request, task_id):
    task = ChecklistTask.objects.get(id=task_id)
    task.status = "rejected"
    task.save()
    return redirect("checklist_dashboard", page_id=task.page_id)
