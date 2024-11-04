from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
        Form for adding comments to blog posts.
        Uses Django's built-in ModelForm for simplicity.
    """
    class Meta:
        model = Comment
        fields = ("body",)
    class Meta:
        model = Comment
        fields = ("body",)
