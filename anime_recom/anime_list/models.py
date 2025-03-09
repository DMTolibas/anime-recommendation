from django.db import models
from multiselectfield import MultiSelectField

# created on amrch72025Create your models here.
class Anime(models.Model):

   ANIME_GENRE = (
    ("ACTION", "Action"),
    ("ADVENTURE", "Adventure"),
    ("COMEDY", "Comedy"),
    ("DRAMA", "Drama"),
    ("FANTASY", "Fantasy"),
    ("HORROR", "Horror"),
    ("MAGIC", "Magic"),
    ("MECHA", "Mecha"),
    ("MYSTERY", "Mystery"),
    ("PSYCHOLOGICAL", "Psychological"),
    ("ROMANCE", "Romance"),
    ("SCI_FI", "Sci-Fi"),
    ("SLICE_OF_LIFE", "Slice of Life"),
    ("SPORTS", "Sports"),
    ("SUPERNATURAL", "Supernatural"),
    ("THRILLER", "Thriller"),
    ("HISTORICAL", "Historical"),
    ("MARTIAL_ARTS", "Martial Arts"),
    ("MUSIC", "Music"),
    ("PARODY", "Parody"),
    ("GAME", "Game"),
    ("DEMONS", "Demons"),
    ("SHOUNEN", "Shounen"),
    ("SHOUJO", "Shoujo"),
    ("SEINEN", "Seinen"),
    ("JOSEI", "Josei"),
    ("HAREM", "Harem"),
    ("REVERSE_HAREM", "Reverse Harem"),
    ("MILITARY", "Military"),
    ("VAMPIRE", "Vampire"),
    ("POLICE", "Police"),
    ("SAMURAI", "Samurai"),
    ("KIDS", "Kids"),
    )
   
   title = models.CharField(max_length=200)

   genre = MultiSelectField(max_length=50,
                  choices=ANIME_GENRE)
   
   num_ep = models.IntegerField(default=12)
   completed = models.BooleanField(default="FALSE")


   def __str__(self):
      return self.title

   


    