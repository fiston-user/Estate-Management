from django.contrib import admin
from django.conf import settings
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Equalis Apartments API",
        default_version="v1",
        description="An API for Equalis Apartments",
        contact=openapi.Contact(email="contact@equalis.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Equalis Apartments Admin"
admin.site.site_title = "Equalis Apartments Admin Portal"
admin.site.index_title = "Welcome to Equalis Apartments Admin Portal"
