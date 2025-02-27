from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    sub_title = models.CharField(max_length = 255)
    content = models.TextField()
    post_by = models.CharField(max_length = 255)
    post_image = models.ImageField(upload_to = 'post_images/')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.title
