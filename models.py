from django.db import models

class Country(models.Model):
    iso = models.CharField(
      unique=True,
      max_length=126,
      help_text="ISO two-character id for the country.",
      )
      
    name = models.CharField(
      max_length=126,
      help_text="Name of the country.",
      )

    def __str__(self):
      return "{0} {1}".format(
      self.iso, self.name
      ) 



class BibleBooks(models.Model):
    james = models.CharField(
      max_length=64,
      help_text="King James Bible title for the book.",
      )
    
    vulgate = models.CharField(
      max_length=64,
      help_text="Vulgate reference for the book.",
      )

    dv = models.CharField(
      max_length=64,
      help_text="Douay Rheims reference for the book.",
      )

    auth = models.CharField(
      max_length=126,
      help_text="Full title reference in the Authorised Version for the book.",
      )

    def __str__(self):
      return "{0}".format(
      self.james
      )      



class Color(models.Model):
    name = models.CharField(
      db_index=True,
      unique=True,
      max_length=126,
      help_text="Machine name for the color.",
      )
      
    title = models.CharField(
      max_length=126,
      help_text="Display for the color.",
      )

    hex = models.CharField(
      max_length=32,
      help_text="Hex code for the color.",
      )
      
    rgb = models.CharField(
      max_length=32,
      help_text="RGB code for the color.",
      )

    def __str__(self):
      return "{0}".format(
      self.name
      )      
      
      
class Tree(models.Model):
    title = models.CharField(
      db_index=True,
      max_length=126,
      help_text="Common name for the tree.",
      )
    
    latin = models.CharField(
      max_length=126,
      db_index=True,
      unique=True,
      help_text="Latin name for the tree.",
      )

    def __str__(self):
      return "{0}".format(
      self.title
      )


      
class Mineral(models.Model):
    name = models.CharField(
      max_length=64,
      help_text="Name for the mineral.",
      )
    
    isvalid = models.BooleanField(
      max_length=126,
      help_text="Is a recognised species of mineral.",
      )

    reason = models.CharField(
      max_length=256,
      help_text="Reason, if given, why not valid.",
      )
      
    def __str__(self):
      return "{0}".format(
      self.name
      )



class Star(models.Model):
    name = models.CharField(
      db_index=True,
      max_length=126,
      help_text="Common name for the star.",
      )
    
    distance = models.DecimalField(
      help_text="Distance to the star, in parsecs.",
      max_digits=15,
      decimal_places=10
      )
      
    magnitude = models.DecimalField(
      help_text="Apparent visual magnitude of the star",
      max_digits=4,
      decimal_places=2
      )

    spectrum = models.CharField(
      max_length=126,
      help_text="Light spectrum for the star.",
      )
      
    color = models.DecimalField(
      help_text="Color index of the star.",
      max_digits=4,
      decimal_places=3
      )
      
    def __str__(self):
      return "{0}-{1}".format(
      self.pk, self.name
      )
