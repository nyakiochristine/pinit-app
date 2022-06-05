from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    path('account/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path(r'^search/',views.search,name='search'),
]