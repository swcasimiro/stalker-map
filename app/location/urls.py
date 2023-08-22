from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('test', views.hood_list, name='Location'),
    path('base/', views.hood_list, name='location'),
    path('base/username', TemplateView.as_view(template_name="location/info_location.html"), name='info_location'),
    path('base/<int:pk>', views.HoodView.as_view(), name='stats'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)