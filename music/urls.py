from django.urls import path
from . import views
from .views import loginclass
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name='music'
urlpatterns = [
    path('home/', views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.loginclass.as_view(),name='signin'),
    path('logout/',views.logout,name='logout'),
    path('history/',views.history.as_view(),name='history'),
    path('song/<int:id>',views.playsong,name='song'),
    path('addsong/',views.add.as_view(),name='addsong'),
    path('manage/',views.admin,name='manage'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/',views.search,name='search')
]
loginclass.as_view()