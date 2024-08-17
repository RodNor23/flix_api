from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermition


class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
