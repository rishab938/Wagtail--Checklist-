from django.shortcuts import render
from wagtail.models import Page

def published_pages(request):
    pages = (
        Page.objects.live()
        .public()
        .specific()
        .exclude(depth=1)
        .exclude(title="Home")
    )
    return render(request, "home/published_pages.html", {"pages": pages})
