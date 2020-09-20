from django.db import models
from django.utils.timezone import now

# Create your models here.
class module_feed(models.Model):
    ad_title=models.TextField(max_length=1000,null=True)
    orgv_url=models.URLField(max_length=1000,null=True)
    ad_url=models.URLField(max_length=1000,null=True)
    ad_unlisted=models.CharField(max_length=100,null=True)
    upload_date = models.CharField(max_length=200,null=True)
    ad_genre=models.TextField(max_length=1000,null=True)
    view_count=models.IntegerField(null=True)
    length=models.CharField(max_length=30,null=True)
    ad_likes=models.CharField(max_length=1000,null=True)
    ad_dislikes=models.CharField(max_length=1000,null=True)
    ad_cta_link=models.URLField(max_length=2000,null=True)
    ad_description=models.TextField(max_length=10000,null=True)
    ad_links=models.TextField(max_length=1000,null=True)
    count=models.IntegerField(null=True)
    channel_name=models.CharField(max_length=1000,null=True)
    ad_channel_link=models.URLField(max_length=1000,null=True)
    subscribers=models.IntegerField(null=True)
    creation_date = models.CharField(max_length=1000,null=True,)
    total_videos=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.ad_title
