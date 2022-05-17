from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='post_images/')

    def get_summary(self):
        return self.text[:70] + '...'

