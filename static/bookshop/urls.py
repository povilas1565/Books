from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/', include('app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    url(r'^accounts/',include('django.contrib.auth.urls')),
]