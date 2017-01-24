from django.db import models
from wagtail.wagtailcore.models import Page


class BlogRoll(Page):
    subpage_types = ["BlogPost"]

    def get_context(self, request):
        context = super().get_context(request)
        posts = self.get_children().live()
        context["posts"] = posts
        return context

class BlogPost(Page):
    pass
