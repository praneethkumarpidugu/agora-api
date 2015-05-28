from django.conf.urls import include, url
from rest_framework.authtoken import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


page_list = views.PageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

page_detail = views.PageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create_comment'
})

comment_list = views.CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = views.CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create_user'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^pages/?$',
        page_list,
        name='page-list'),
    url(r'^pages/(?P<id>[^/]+)/?$',
        page_detail,
        name='page-detail'),
    url(r'^pages/(?P<id>[^/]+)/comments/?$',
        comment_list,
        name='page-comments'),
    url(r'^comments/(?P<id>[^/]+)/?$',
        comment_detail,
        name='comment-detail'),
    url(r'^users/?$',
        user_list,
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/?$',
        user_detail,
        name='user-detail')
])

urlpatterns += [
    url(r'^auth/token/?$', auth_views.obtain_auth_token, name='auth-token'),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
]
