from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest


class TestAboutViews(TestCase):
    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me."
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verified get request for about me containing a collaboration form"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIsInstance(
            response.context["collaborate_form"], CollaborateForm
        )

    def test_sucessful_collaborate_submission(self):
        """Test for collaboration request submission"""
        self.client.login(username="myUsername", myPassword="myPassword")
        post_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "message": "I'd like to collaborate on this project.",
        }
        response = self.client.post(reverse("about"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content,
        )
