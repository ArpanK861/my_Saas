"""
URL configuration for sashome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#from .views import my_old_home_page_view

#from .views import my_old_home_page_view1

#from .views import my_home_page_view

from .views import *

urlpatterns = [
    path("", my_home_page_view), #index page -> root page
    path("page view", my_home_page_view),
    path("Hello", my_old_home_page_view2),
    path("Hello-world", my_old_home_page_view1),
    path("Hello-world.html", my_old_home_page_view),
    path("admin/", admin.site.urls),
]
