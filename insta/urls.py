from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.welcome,name='welcome'),
    url('^search/', views.search_category,name='search_category'),
    url(r'^photo/(\d+)',views.single_photo,name='photo'),
    url(r'^new/image$',views.new_image,name='new-image'),
    url(r'^new/profile$',views.new_profile,name='new-profile'),
    url(r'^updateprofile$',views.update_profile,name='updateprofile'),
    url(r'^comment$',views.makecomment,name='makecomment'),
    url('^like$', views.like_a_post,name='like_a_post'),
    url('^follow$',views.follow,name='follow'),
    url('^delete/(?P<post_id>\d+)$',views.delete_post,name='delete'),
    url(r'^displayprofile/(?P<user_id>\d+)$',views.display_profile,name='displayprofile')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)