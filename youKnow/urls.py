"""
URL configuration for youKnow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from you_know.urls import users_origin_router, users_router, libraries_router, categories_router, keywords_router, tags_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    #path('admin/', admin.site.urls),

    # SwaggerUI
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path('api/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc",),

    # endpoints
    path('', include('you_know.urls')),
    path('api/', include(users_origin_router.urls)),
    path('api/', include(users_router.urls)),
    path('api/', include(libraries_router.urls)),
    path('api/', include(categories_router.urls)),
    path('api/', include(keywords_router.urls)),
    path('api/', include(tags_router.urls)),
]
