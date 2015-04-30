from django.shortcuts import render
from django.contrib.auth.models import User
import django_filters

from rstApi.models import VideoData
from rstApi.serializers import UserSerializer,VideoSerializer
from rstApi.permissions import IsOwnerOrReadOnly,IsAdminOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import filters
import pdb


class VideoFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(name="name", lookup_type='contains')
    class Meta:
        model = VideoData
        fields = ['search','popularity','director','genere','imdb_score','owner']

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoData.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    filter_class = VideoFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username', 'email')


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'rstApi': reverse('videodata-list', request=request, format=format)
    })