
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Pizza Delivery API",
        default_version='v1',
        description="A REST API Pizza delivery service",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>.json|.yaml', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]
