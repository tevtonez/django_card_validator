"""main app urls."""
from django.conf.urls import url
from main.views import checksum

app_name = 'main'

urlpatterns = [
    url(r'^check_number/$', checksum, name='check'),
]
