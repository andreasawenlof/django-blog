from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
        Admin interface for managing the about page content and profile image.
    """
    summernote_fields = ("content",)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(SummernoteModelAdmin):
    """
        Admin interface for managing collaborate request form submissions.
    """
    list_display = (
        "name",
        "read",
    )
