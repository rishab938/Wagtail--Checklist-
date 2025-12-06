from wagtail import hooks
from wagtail.admin.panels import Panel, ObjectList
from .models import ChecklistTask


class ChecklistPanel(Panel):
    template = "checklist/panel.html"

    def get_context_data(self, parent_context=None):
        page = parent_context["page"]
        tasks = ChecklistTask.objects.filter(page=page)

        return {
            "page": page,
            "page_id": page.id,
            "tasks": tasks,
        }


@hooks.register("construct_page_editor")
def add_checklist_tab(context, request):
    page = context["page"]
    edit_handler = context["edit_handler"]

    checklist_tab = ObjectList(
        [ChecklistPanel()],
        heading="Checklist",
        classname="checklist-tab",
    ).bind_to(model=type(page))

    new_tabs = []
    for tab in edit_handler.children:
        new_tabs.append(tab)
        if tab.heading == "Promote":
            new_tabs.append(checklist_tab)

    edit_handler.children = new_tabs


from django.urls import reverse
from wagtail.admin.widgets import Button

@hooks.register('register_page_header_buttons')
def page_header_buttons(page, user, view_name, next_url=None):
    if page.pk:
        url = reverse('checklist_dashboard', args=[page.pk])
        yield Button(
            "Checklist",
            url,
            icon_name="tick",
            priority=80,
            attrs={'target': '_blank', 'title': 'View Checklist Dashboard'}
        )


from wagtail.admin.userbar import BaseItem

class ChecklistUserBarItem(BaseItem):
    def __init__(self, page):
        self.page = page

    def render(self, request):
        url = reverse('checklist_dashboard', args=[self.page.pk])
        return f"""
        <li class="wagtail-userbar__item " role="presentation">
            <a href="{url}" role="menuitem" class="wagtail-action wagtail-icon wagtail-icon-tick">
                Checklist
            </a>
        </li>
        """

@hooks.register('construct_wagtail_userbar')
def add_checklist_userbar_item(request, items):
    page = None
    for item in items:
        if hasattr(item, 'page'):
            page = item.page
            break
    
    if page:
        items.append(ChecklistUserBarItem(page))
