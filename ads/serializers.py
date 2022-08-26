from rest_framework import serializers

from ads.models import Ads, Category


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'