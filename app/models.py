from django.contrib.auth.models import AbstractUser
from django.db import models

from boring_interiors import settings


class Style(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    style = models.ManyToManyField(Style, related_name="styles")
    proj_img = models.ImageField(upload_to=f"img/title/", default=None)

    def __str__(self) -> str:
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=63)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"img/content/")

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass


class Commentary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
