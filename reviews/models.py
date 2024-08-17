from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):

    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'O valor deve ser superior a 0'),
        MaxValueValidator(5, 'O valor deve ser inferior a 5'),
    ])

    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.movie)
