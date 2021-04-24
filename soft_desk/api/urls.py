from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api import views as api_view

urlpatterns = [
    path('signup/', api_view.register, name ="register" ),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', api_view.projects_list, name='projects_list'),
]