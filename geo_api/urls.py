from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from geo_api import views
from geo_api.views import FileUploadView

router = routers.DefaultRouter()
router.register(r'polygon', views.PolygonViewSet, basename='polygon')
router.register(r'linestring', views.LineStringViewSet, basename='linestring')
router.register(r'point', views.PointViewSet, basename='point')
router.register(r'upload', views.UploadViewSet, basename="upload")
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)