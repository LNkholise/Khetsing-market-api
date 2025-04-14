from rest_framework import generics
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Listing
from rest_framework.permissions import IsAuthenticated, AllowAny
from  allauth.socialaccount.models import SocialAccount, SocialToken
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .serializers import ListingsSerializer, ListingDetailSerializer, UserSerializer


# View to create a new user
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        # Get the user object based on the authenticated user
        return self.request.user

@ login_required
def google_login_callback(request):
    user = request.user

    # for debuging reasons, don't pass into production
    social_accounts = SocialAccount.objects.filter(user=user).first()
    print("Social Account: ", social_accounts)

    social_account = social_accounts.first()

    if not social_account:
        print("No social account found.")
        return redirect('http://localhost:3000/login/callback/?error=NoSocialAccount')
    
    token = SocialToken.objects.get(account=social_account, account_providers='google').first()

    if token:
        print('Google token found:', token.token)
        refresh = RefreshToken.for_user(user)
        return redirect(f'http://localhost:3000/login/callback/?token={token.token}&refresh={refresh.access_token}')
    else:
        print('No Google user found for user', user)
        return redirect('http://localhost:3000/login/callback/?error=NoGoogleUser')
    
@csrf_exempt
def validate_google_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = data.get('token')
            print('Google Token:', token)

            if not token:
                return JsonResponse({'error': 'Token is required'}, status=400)
            return JsonResponse({'valid': True}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'detail': 'Method not allowed'}, status=405)

# View to list all listings (previews only)
class ListingsView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingsSerializer
    permission_classes = [AllowAny]

# View to show full details using the slug
class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

