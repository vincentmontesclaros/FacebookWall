from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, related_name='author')
    content = models.CharField(
        max_length=255,
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='likers')

    # def __unicode__(self):
    #     return self.content

    # def get_absolute_url(self):
    #     return reverse('content', kwargs={'pk': self.pk})
