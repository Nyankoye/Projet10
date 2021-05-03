from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api import views as api_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects',api_view.ProjectView, basename='Project')
router.register(prefix=r'projects/(?P<project_id>\d+)/users', viewset=api_view.ContibutorView, basename='Contributor')
router.register(prefix=r'projects/(?P<project_id>\d+)/issues', viewset=api_view.IssueView, basename='Issue')
router.register(prefix=r'projects/(?P<project_id>\d+)/issues/(?P<issue_id>\d+)/comments', viewset=api_view.CommentView, basename='Comment')

urlpatterns = [
    path('signup/', api_view.RegisterView.as_view(), name ="register" ),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]