"""tdrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from rest_framework.compat import yaml
from rest_framework.renderers import JSONOpenAPIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view
from rest_framework.utils import json, encoders


def render(self, data, media_type=None, renderer_context=None):
    return json.dumps(data, indent=2, cls=encoders.JSONEncoder).encode('utf-8')


def render2(self, data, media_type=None, renderer_context=None):
    data = json.loads(json.dumps(data, cls=encoders.JSONEncoder))
    return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True).encode('utf-8')
    
    
JSONOpenAPIRenderer.render = render
OpenAPIRenderer.render = render2

urlpatterns = [
    path('tapp/', include('tapp.urls')),
    path('openapi/', get_schema_view(title='XXX API Document', description=_('test desc')), name='openapi'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
]
