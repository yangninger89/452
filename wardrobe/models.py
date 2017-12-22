from django.db import models
from django.utils import timezone



class Post(models.Model):  # I decided to define each clothes (every post) object by specifying owner, type, description, created_date, and published_date
    owner = models.ForeignKey('auth.User')
    type = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.type

