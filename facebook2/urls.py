"""facebook2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('profile/', views.profile, name='profile-page'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('createpost/', views.createpost, name='createpost'),
    path('editpost/<int:id>', views.editpost, name='editpost'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost'),

    path('api/stories', views.stories, name='stories'),

    path('vuetest', views.vuetest, name='vuetest'),
    path('vuehomepage', views.vuehomepage, name='vuehomepage'),

    path('sw.js', (
        TemplateView.as_view(
        template_name="sw.js",
        content_type='application/javascript')), name='sw.js')
]
