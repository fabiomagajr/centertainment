from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    GENDER_CHOICES=[('Male','Male'),('Female','Female'),('Other','Other')]
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    GENDER_CHOICES=[('Male','Male'),('Female','Female'),('Other','Other')]
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    golden_globes_won = models.IntegerField(default=0)
    oscar_nominations = models.IntegerField(default=0)
    oscar_won = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_synopsis = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    minimum_age = models.IntegerField()
    duration=models.IntegerField(help_text="Duration in minutes")
    is_adult = models.BooleanField(default=False)
    release_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    golden_globes_won = models.IntegerField(default=0)
    oscar_nominations = models.IntegerField(default=0)
    oscar_won = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.name} in {self.movie.title}"


