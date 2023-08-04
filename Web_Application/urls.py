"""
URL configuration for Web_Application project.

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
from django.urls import path
from Admin_web import views as appview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Admin_page",appview.Admin_page,name="Admin_page"),
    path("",appview.Login,name="Login"),
    path("User_login",appview.User_login,name="User_login"),
    path("User_reg",appview.User_reg,name="User_reg"),
    path("user_page",appview.user_page,name="user_page"),
    # path('mysession//(?P<pk>\d+)/$',appview.appsession,name="mysession")
    path('logout',appview.logout,name='logout'),
]
