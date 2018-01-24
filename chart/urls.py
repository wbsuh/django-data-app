from django.conf import settings
from django.conf.urls import url
from chart import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
] + static(settings.STATIC_ROOT)