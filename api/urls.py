from django.urls import path
from .views import ListingsView, ListingDetailView, UserCreateView, UserDetailView, google_login_callback, validate_google_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include

urlpatterns = [
    path('listings/', ListingsView.as_view(), name='listing-list'),
    path('listings/<slug:slug>', ListingDetailView.as_view(), name='listing-detail'),
    path('user/register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('callback/', google_login_callback, name='google-login-callback'),
    path('auth/user/', UserDetailView.as_view(), name='user-detail'),
    path('google/validate_token', validate_google_token, name='validate-google-token'),
]
