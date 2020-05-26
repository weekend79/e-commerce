from django.conf.urls import url, include
from . import url_reset
from .views import index, logout, login, register, profile


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^password_reset_confirm/', include(url_reset)),
    url(r'^password_reset_done/', include(url_reset)),
    url(r'^password_reset_complete/', include(url_reset)),
]
