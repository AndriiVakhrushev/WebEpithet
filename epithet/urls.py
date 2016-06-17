from django.conf.urls import url
from django.contrib import admin

from epithet import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^get_epithet/$', views.get_epithet, name='get_epithet'),

]
