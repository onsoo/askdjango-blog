"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings 
# from django.conf.urls import settings 
from django.urls import include, path, re_path
from django.shortcuts import redirect

# def root(request):
#     return redirect('blog:post_list')


urlpatterns = [
    # path('', root, name='root'),
    path('', lambda r: redirect('blog:post_list'), name='root'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('dojo/', include('dojo.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        re_path(r'^__debug__/', include(debug_toolbar.urls)), 
    ]