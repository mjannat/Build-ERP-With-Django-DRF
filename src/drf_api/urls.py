from django.contrib import admin
from django.urls import include, path

from core.views import TestView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('post/', TestView.as_view()),
]
