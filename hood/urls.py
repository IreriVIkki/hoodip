from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^leave/hood/(\d+)$', views.leave_hood, name='leave_hood'),
    url(r'^delete/business/(\d+)$', views.delete_business, name='delete_business'),
    url(r'^join/hood/(\d+)$', views.join_hood, name='join_hood'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^search/$', views.search_results, name='search_results'),
    # url(r'^new/post/$', views.post_website, name='post_website'),
    url(r'^userdetails/(\d+)/(\w+)/$', views.edit_profile, name='edit_profile'),
    # url(r'^rate/post/(\d+)$', views.rate_website, name='rate_website'),
]

# this will help to serve uploaded images on the development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
