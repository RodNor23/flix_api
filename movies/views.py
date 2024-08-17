from rest_framework import generics, views, response, status
from django.db.models import Count, Avg
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermition
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        total_reviews = Review.objects.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={'total_movies': total_movies,
                  'total_reviews': total_reviews,
                  'movies_by_genre': movies_by_genre,
                  'average_stars': round(average_stars, 1) if average_stars else 0,
                  },
            status=status.HTTP_200_OK,
        )
