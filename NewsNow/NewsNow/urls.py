"""newspage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from main.sitemap import MyNewsSiteMap
from rest_framework import routers
from main import views

router =  routers.DefaultRouter()
router.register(r'mynews', views.NewsViewSet)

sitemaps = {
    'news': MyNewsSiteMap(),
}
urlpatterns = [

    url(r'rest/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^sitemap\.xml$', sitemap,{'sitemaps':sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
    # path('media/<path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('static/<path>/', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('',include('main.urls')),
    path('',include('news.urls')),
    path('',include('cat.urls')),
    path('', include('subcat.urls')),
    path('', include('contactform.urls')),
    path('', include('trending.urls')),
    path('', include('manager.urls')),
    path('', include('newsletter.urls')),
    path('', include('comment.urls')),
    path('', include('blacklist.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
