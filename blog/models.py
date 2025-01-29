from typing import List
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    """This is the child model for the blog posts.

    Args:
        models (models.Model): The django model.

    Returns:
        Post: An object of this class.
    """
    author: models.ForeignKey = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title: models.CharField = models.CharField(max_length=200)
    text = models.TextField()
    created_date: models.DateTimeField = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        """Publish a blog post.
        """
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self) -> List[models.CharField]:
        """Get the list of approved comments by title.

        Returns:
            List[models.CharField]: A list of approved comments.
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self) -> str:
        """Get the url to be redirected to.

        Returns:
            str: The redirect url.
        """
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        """Return the a string reprsenting the object of this class.

        Returns:
            str: The title of this class.
        """
        return self.title


class Comment(models.Model):
    """This is the class for making comments.

    Args:
        models (models.Model): This is the class that this class inherits from.

    Returns:
        Comment: An object of this class.
    """
    post: models.ForeignKey = models.ForeignKey("blog.post", related_name="comments", on_delete=models.CASCADE)
    author: models.CharField = models.CharField(max_length=200)
    text: models.TimeField = models.TextField()
    created_date: models.DateTimeField = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approved_comment: models.BooleanField = models.BooleanField(default=False)

    def approve(self) -> None:
        """Appove a comment.
        """
        self.approved_comment = True
        self.save()

    def get_absolute_url(self) -> str:
        """Get the reverse url.

        Returns:
            str: The reverse url.
        """
        return reverse("post_list")

    def __str__(self) -> str:
        """Return the a string reprsenting the object of this class.

        Returns:
            str: The text of the blog post.
        """
        return self.text
