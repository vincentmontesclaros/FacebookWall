from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.CharField(
        max_length=255,
    )
    pub_date = models.DateTimeField('date published')
    # user, user_id --> the one who posted the post
	# likes. user_id of the likers
