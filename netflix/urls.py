from django.conf import settings
from django.contrib import admin

from django.urls import path
from django.urls import include
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Movie  Rest Api",
        default_version="v1",
        description="Swagger docs for Rest Api",
        contact=openapi.Contact("Xalimov Abdulla <player2020uz@gmail.com>"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('netflixapp.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-docs"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc-docs"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)