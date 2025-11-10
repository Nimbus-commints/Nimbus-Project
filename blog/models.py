from django.db import models
from django.urls import reverse

"""
reverse allows  us to reference an object by its URL template.
"""


# Create your models here.
# Aca se esta creando una subclass de models llamada Blogs que permite el acceso
# a todo dentro de django.db.models.Models
class Blog(models.Model):
    # modeo con 3 diferentes campos.
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
