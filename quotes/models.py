from django.db import models


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=150)
    quote = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.author
