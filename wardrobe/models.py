from django.db import models
from django.utils import timezone



class Post(models.Model):
    owner = models.ForeignKey('auth.User')
    type = models.CharField(max_length=200)
    description = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_data = timezone.now()
        self.save()


    def __str__(self):
        return self.type

