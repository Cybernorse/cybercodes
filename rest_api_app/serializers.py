from rest_framework import serializers
from .models import module_feed

class moduleserializer(serializers.ModelSerializer):
    class Meta:
        model=module_feed
        fields=(
        'id',
        'url',
        'ad_title',
        'orgv_url',
        'ad_url',
        'ad_unlisted',
        'upload_date',
        'ad_genre',
        'view_count',
        'length',
        'ad_likes',
        'ad_dislikes',
        'ad_cta_link',
        'ad_description',
        'ad_links',
        'count',
        'channel_name',
        'ad_channel_link',
        'subscribers',
        'creation_date',
        'total_videos',
        )
