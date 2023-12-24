from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
    path('cancelled/', TemplateView.as_view(template_name='cancelled.html')),
    path('success/', TemplateView.as_view(template_name='success.html')),
]
