from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
import uuid

# Create your models here.
class Profile(models.Model):
    profile_uuid = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)    
    profile_slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        self.user_name = slugify(self.user.first_name)        
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)