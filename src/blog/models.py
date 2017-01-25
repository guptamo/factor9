from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class BlogRoll(Page):
    subpage_types = ["BlogPost"]

    def get_context(self, request):
        context = super().get_context(request)
        posts = self.get_children().live()
        context["posts"] = posts
        return context


class BlogPost(Page):
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    promote_panels = Page.promote_panels + [
        ImageChooserPanel("feed_image")
    ]
