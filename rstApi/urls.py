from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rstApi import views

urlpatterns = [
    url(r'^rstApi/$', views.VideoList.as_view(),name='rstApi-list'),
    url(r'^rstApi/(?P<pk>[0-9]+)/$', views.VideoDetail.as_view(),name='rstApi-detail'),
    url('^movieList/(?P<username>.+)/$', views.MovieList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)