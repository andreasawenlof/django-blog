from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
        Form for adding comments to blog posts.
        Uses Django's built-in ModelForm for simplicity.
    """
    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message")
