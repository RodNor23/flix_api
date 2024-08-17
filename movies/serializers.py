from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('We accept only movies oldest than 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Text field accept only 200 characters')
        return value


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'actors', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
