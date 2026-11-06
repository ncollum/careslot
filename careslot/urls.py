from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('admin/', admin.site.urls),
  # Django's login, logout and password reset views, without a namespace
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include('accounts.urls')),
  path('doctors/', include('doctors.urls')),
  path('appointments/', include('appointments.urls')),
  path('records/', include('records.urls')),
  path('articles/', include('articles.urls')),
  path('', include('core.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
