from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import login_view
from gamestore import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', login_view, name='login'),
    path('tovar', views.tovar, name='tovar'),
    path('novosti', views.novosti, name='novosti'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
