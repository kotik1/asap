from django.conf.urls import include, url
from django.contrib import admin
from app.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.intro, name='intro'),
    url(r'^login/$', views.login),
    url(r'^sign_up/$', views.sign_up),
    # url(r'^add/$', views.add),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^add/$', views.add, name='add'),
    url(r'^mark_done/$', views.mark_done, name='mark_done'),
    url(r'^mark_undone/$', views.mark_undone),
    url(r'^delete/$', views.delete),
    url(r'^edit/$', views.edit),
    url(r'^logout/$', views.logout),
    url(r'^done/$', views.done),
]
