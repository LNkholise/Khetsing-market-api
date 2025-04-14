from rest_framework import serializers
from .models import Listing, KhetsingUser

# Minimal serializer for previews
class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'price', 'description', 'image_1', 'slug', 'listing_type']

# Full serializer for detailed view
class ListingDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()  # Show the username of the owner

    class Meta:
        model = Listing
        fields = '__all__'

# Have a serializer for the User Accounts
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhetsingUser
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = KhetsingUser.objects.create_user(**validated_data)
        return user 
