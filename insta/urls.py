from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.welcome,name='welcome'),
    url('^search/', views.search_category,name='search_category'),
    url(r'photo/(\d+)',views.single_photo,name='photo'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)