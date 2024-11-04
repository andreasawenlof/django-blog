from django.urls import path
from . import views

urlpatterns = [
    """
        Create URL patterns for blog posts.

        This includes a list view for all blog posts, a detail view for a specific post,
        and views for editing and deleting comments on a post.
    """,
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]
