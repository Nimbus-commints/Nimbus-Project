from django.test import TestCase  # TO test Databases
from django.urls import reverse
from .models import Post  # added

# Create your tests here.


class PostTests(TestCase):  # added
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    # url exist, name available, template correct, content
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts.html")
        self.assertContains(response, "This is a test!")


# better to use the test_homepage(self)
# def test_url_available_by_name(self):
#     response = self.client.get(reverse("posts"))
#     self.assertEqual(response.status_code, 200)

# def test_template_name_correct(self):
#     response = self.client.get(reverse("posts"))
#     self.assertTemplateUsed(response, "posts.html")

# def test_template_content(self):
#     response = self.client.get(reverse("posts"))
#     self.assertContains(response, "This is a test!")
