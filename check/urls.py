from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_main, name='item_main'),
    #url(r'^search/(?P<text>[[\w]+)/$', views.item_search, name='item_search'),
    url(r'^search/$', views.item_search, name='item_search'),
    url(r'^update/$', views.item_update, name='item_update'),
]