"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp.views import create_database,list_database,update_database,delete_database

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/create',create_database),
    path('demo/list',list_database),
    path('demo/<int:pk>/update',update_database),
    path('demo/<int:pk>/delete',delete_database)
    
    # path('blog/<int:comment_id>/',detail,name='detail'),
    # path('<int:b_id>/',get_data,name='data'),
]