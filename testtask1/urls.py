"""testtask1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from testnews.views.news_list import NewsView, OneNewsView
from testnews.views.add_forms import NewsCreateView

urlpatterns = [
    # News urls
    url(r'^$', NewsView.as_view(), name='home'),
    url(r'^news/(?P<pk>\d+)$', OneNewsView.as_view(), name='one_news_show'),
    url(r'^news/add/$', NewsCreateView.as_view(), name='add_news'),
    url(r'^news/(?P<pk>\d+)/comment/$', 'testnews.views.add_forms.add_comment', name='add_comment'),



    url(r'^admin/', include(admin.site.urls)),
]
