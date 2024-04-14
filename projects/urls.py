from django.urls import path
from . import views

from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    path("cv/", views.cv, name="cv"),
    path("contact/", views.contact, name="contact"),
    path("success/", views.success, name="success"),
    path("works/", views.works, name="works"),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]

