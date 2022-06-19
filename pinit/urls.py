from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path(r'postImage/',views.post_image,name='postImage'),
    path(r'user/(?<username>\w+)',views.profile,name='profile'),
    path(r'user/account/edit/',views.edit_profile,name='editProfile'),
    path(r'image/(?P<image_id>\d+)',views.view_single_image,name='singleImage'),
    path(r'search/',views.search,name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)