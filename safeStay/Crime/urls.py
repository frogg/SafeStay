__author__ = 'larissa'
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'Crime.views.get_crimes'),
]