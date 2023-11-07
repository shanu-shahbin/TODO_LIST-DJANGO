from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]
