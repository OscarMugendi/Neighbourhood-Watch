from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update/', views.update_profile, name='update_profile'),
    path('hoods/', views.hoods, name='hoods'),
    path('hood/<hood_id>/', views.hood, name='hood'),
    path('join_hood/<id>/', views.join_hood, name='join_hood'),
    path('leave_hood/<id>/', views.leave_hood, name='leave_hood'),
    path('hood/<hood_id>/new_business/', views.new_business, name='business'),
    path('hood/<hood_id>/new_post/', views.new_post, name='post'),
    path('hood/<hood_id>/neighbours/', views.neighbours, name='neighbours'),
    path('search/', views.search_business, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)