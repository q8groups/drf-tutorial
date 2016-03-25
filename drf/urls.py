"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.authtoken import views
from registration.views import UserList,GenricUserList,GenricCompanyList,GenricCompanyObject

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^edara/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/users/', UserList.as_view()),
    url(r'^api/gusers/', GenricUserList.as_view()),
            url(r'^api/company/$', GenricCompanyList.as_view()),

        url(r'^api/company/(?P<pk>[0-9]+)/$',GenricCompanyObject.as_view()),




]





