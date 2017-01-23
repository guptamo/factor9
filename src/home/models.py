from __future__ import absolute_import, unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):

    subpage_types = ["HomePageChild"]

    def get_context(self, request):
        context = super().get_context(request)
        children = self.get_children().live().order_by('-first_published_at')
        context['kids'] = children
        return context

class HomePageChild(Page):
    body = RichTextField(blank=False)
    name = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("name", classname="full"),
    ]
