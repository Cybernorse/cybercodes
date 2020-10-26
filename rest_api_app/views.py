from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .serializers import moduleserializer
from .models import module_feed

class ModuleView(viewsets.ModelViewSet):
    queryset=module_feed.objects.all()
    serializer_class=moduleserializer
    permission_classes=(permissions.DjangoModelPermissionsOrAnonReadOnly,)
    
    def upload_dates1(request):
        queryset=module_feed.objects.all().order_by('-upload_date')
    
    def view_counts1(request):
        queryset=module_feed.objects.all().order_by('-view_count')

    def yesterdays1(request):
        queryset=module_feed.objects.all().order_by('-yesterday')

    def lastdays1(request):
        queryset=module_feed.objects.all().order_by('-last_30_days')

    def length1(request):
        queryset=module_feed.objects.all().order_by('-length')

        
    # ordering_fields = [
    #     'id',
    #     'url',
    #     'video_file',
    #     'upload_date',
    #     'view_count',
    #     'yesterday',
    #     'last_30_days',
    #     'length',
    #     'channel_name',
    #     ]
    
