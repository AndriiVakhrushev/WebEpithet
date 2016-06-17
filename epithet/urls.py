from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from epithet import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_epithet/$', views.get_epithet, name='get_epithet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
