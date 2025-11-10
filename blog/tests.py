from django.test import TestCase
from django.contrib.auth import get_user_model  # added
from .models import Blog  # added
from django.urls import reverse  # added


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.blog = Blog.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.blog.title, "A good title")
        self.assertEqual(self.blog.body, "Nice body content")
        self.assertEqual(self.blog.author.username, "testuser")
        self.assertEqual(str(self.blog), "A good title")
        self.assertEqual(self.blog.get_absolute_url(), "/blogs/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blogs/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "blogs.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.blog.pk}))
        no_response = self.client.get("/blogs/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "blog_detail.html")
