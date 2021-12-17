from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=30,blank=False,null=False)
    author=models.CharField(max_length=30,blank=False,null=False)
    image=models.ImageField(upload_to='image/',null=True)
    audio_link=models.FileField(upload_to='audio/',null=True)
    views=models.IntegerField(blank=True,null=True,default='100')
    category = models.CharField(max_length=10, blank=False, default='')
    def __str__(self):
        return self.title

class history_listen(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Song_id=models.CharField(max_length=1000000,)
    create_at=models.DateTimeField(default=timezone.datetime.now())

