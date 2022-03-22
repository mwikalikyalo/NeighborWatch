from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('home/', views.index, name='home'),
  path('', views.profile, name='profile'),
  path('find/', views.find, name='search'),
  path('ajax/search/', views.searchajax, name='searchajax')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)