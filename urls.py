
from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    #path('', views.home, name='home'),
    #path('logout/', views.logout_user, name = 'logout'),
]
