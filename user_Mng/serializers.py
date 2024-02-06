from rest_framework import serializers
from .models import User, Bank
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    cart = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description'
     )

    class Meta:
        model = User
        fields = [
            'uuid',
            'full_name',
            'birthday',
            'phone',
            'bank',
            'bank_acc',
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        max_length=255, min_length=6, write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = User
        fields = [
            'new_password',
        ]

    def update(self, instance, validated_data):
        if validated_data.get("new_password"):
            instance.password = make_password(validated_data["new_password"])
        instance.email = validated_data["email"]
        instance.role = validated_data["role"]
        instance.save()
        return instance


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

    def create(self, validated_data):
        return Bank(**validated_data)
