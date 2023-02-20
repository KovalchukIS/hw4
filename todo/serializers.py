from rest_framework import serializers
from todo.models import List
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class NonModelSerializer(serializers.Serializer):
    """Сериализатор с не-модельными полями."""


class ListSerializer(serializers.ModelSerializer):
    """Сериализатор по модели List."""

    # article_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # article_comments = CommentSerializer(many=True)
    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    # image = Base64ImageField()

    class Meta:
        model = List
        read_only_fields = ["id", "end_dt"]
        fields = read_only_fields + ["name", "is_done"]

    # def create(self, validated_data):
    #     # if not validated_data.get("name"):
    #     #     #User = get_user_model()
    #     #     validated_data["name"] = "Новая Задача"
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     # User = get_user_model()
    #     # author = User.objects.first()
    #     # new_comment = Comment(to_article=instance, author=author, coment="Изменено")
    #     # new_comment.save()
    #     return super().update(instance, validated_data)
