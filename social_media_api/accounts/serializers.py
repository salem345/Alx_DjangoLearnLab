from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
serializers.CharField()

Token.objects.create

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        get_user_model().objects.create_user
        Token.objects.create
        serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'bio', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

def create(self, validated_data):
    validated_data.pop('password2')  # إزالة الحقل المكرر
    User = get_user_model()           # جلب الـUser model المخصص
    user = User.objects.create_user(**validated_data)  # إنشاء مستخدم جديد
    Token.objects.create(user=user)   # إنشاء توكن تلقائي
    return user

User = get_user_model()
class FollowSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'followers_count', 'following_count']

def validate_content(self, value):
    if len(value.strip()) == 0:
        raise serializers.ValidationError("Content cannot be empty.")
    return value