from rest_framework import serializers

from ads.models import Location, Ad


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author',
            'price'
        )
