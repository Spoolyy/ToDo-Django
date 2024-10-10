from django.db import models

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    pub_date = models.DateTimeField("date published: ")
    due_date = models.DateTimeField("due by: ", blank=True, null=True)
    class Priorities(models.IntegerChoices):
        IMPORTANT = 1,
        NORMAL = 2,
        LOWPRIO = 3,
    priority = models.IntegerField(choices=Priorities.choices, default=Priorities.NORMAL)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.content