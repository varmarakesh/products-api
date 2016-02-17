from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from products.view import DetailView, ListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/(?P<id>[0-9]+)/$', DetailView.as_view(), name = 'product detail view'),
    url(r'^products/$', ListView.as_view(), name = 'product list view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
