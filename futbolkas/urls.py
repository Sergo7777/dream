from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from main import views
from .settings import MEDIA_ROOT, DEBUG
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    # Examples:
   
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^item/(?P<alias>[^/]+)', views.item, name='item'),
    url(r'^products$', views.products, name='products'),
    url(r'^dostavka$', views.dostavka, name='dostavka'),
    url(r'^garantia$', views.garantia, name='garantia'),
    url(r'^category/(?P<alias>[^/]+)', views.get_category, name='category'),
    url(r'^place_search/$', views.place_search, name='place_search'),
    #User 
    url(r'^user/logout/$', auth_views.logout, kwargs={'next_page':'home'}, 
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    #url(r'^', include('futbolkas.urls', namespace='main')),    

] 
urlpatterns +=staticfiles_urlpatterns()


