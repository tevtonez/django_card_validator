"""urls."""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from main import views as main_views

# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.IndexView.as_view(), name='home'),
    # url(r'^check_number/$', main_views.checksum, name='check'),

    # app url
    url(r'^api/', include('main.urls')),

]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
