from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home,name='home'),
    path(r'search/',views.search,name='search'),
    path(r'user/(?<username>\w+)',views.profile,name='profile'),
    path(r'postImage/',views.post_image,name='postImage'),
]

#if settings.DEBUG:
    #urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)