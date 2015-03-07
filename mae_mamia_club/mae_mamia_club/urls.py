from django.conf.urls import patterns, include, url
from django.contrib import admin

from members import views as member_views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^members/add/$',
        member_views.MemberAddView.as_view(),
        name='member_add'
    ),
    url(
        r'^members/(?P<member_id>\d+)/$',
        member_views.MemberGenerateImage.as_view(),
        name='member_generate_image'
    ),
    url(
        r'^members/$',
        member_views.MemberView.as_view(),
        name='member'
    ),
)
