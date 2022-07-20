from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'follows', views.FollowViewSet, basename='follows')
router.register( 
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, 
    basename='comments' 
)


urlpatterns = [
    path('v1/', include(router.urls))
]