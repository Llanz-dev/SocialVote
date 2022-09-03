from django.template.defaultfilters import slugify
from accounts.models import Profile
from datetime import datetime
from django.db import models
import uuid
import json

# Create your models here.
class Poll(models.Model):
    poll_creator = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)    
    poll_uuid = models.UUIDField(default=uuid.uuid4)
    poll_img = models.ImageField(blank=True, null=True, upload_to='vote_img')
    question = models.TextField(max_length=65)
    question_slug = models.SlugField(default=None)
    question_one = models.CharField(max_length=30)
    question_two = models.CharField(max_length=30)
    question_three = models.CharField(max_length=30)
    question_one_count = models.IntegerField(default=0)
    question_two_count = models.IntegerField(default=0)
    question_three_count = models.IntegerField(default=0)   
    date_created = models.DateField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.question[:50]

    def set_foo(self, x):
        self.foo = json.dumps(x)

    def get_foo(self):
        return json.loads(self.foo)
    
    def total(self):
        return self.question_one_count + self.question_two_count + self.question_three_count

    def save(self, *args, **kwargs):
        if not self.id:
            self.question_slug = slugify(self.question)
        super(Poll, self).save(*args, **kwargs)