from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Category, Booking, Menu

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'description', 
                 'category', 'category_id', 'featured', 'image']
        extra_kwargs = {
            'price': {'min_value': 0},
            'inventory': {'min_value': 0}
        }

class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    menu_item_ids = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'menu_items', 
                 'menu_item_ids', 'is_active']

    def create(self, validated_data):
        menu_items = validated_data.pop('menu_item_ids', [])
        menu = Menu.objects.create(**validated_data)
        menu.menu_items.set(menu_items)
        return menu

    def update(self, instance, validated_data):
        menu_items = validated_data.pop('menu_item_ids', None)
        if menu_items is not None:
            instance.menu_items.set(menu_items)
        return super().update(instance, validated_data)

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'last_name', 'email', 'phone',
                 'reservation_date', 'reservation_slot', 'guests',
                 'special_requests', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    