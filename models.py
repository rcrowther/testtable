from django.db import models


class ChristmasSong(models.Model):
    gift = models.CharField(
      unique=True,
      max_length=126,
      help_text="Gift for the day.",
      )


    def __str__(self):
      return "pk={} gift={}".format(
      self.pk, self.gift
      )       
      
      
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
      return "iso={} name={}".format(
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
      return "name={} title={}".format(
      self.name, self.title
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
      return "name={} latin={}".format(
      self.title, self.latin
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
      return "name={}".format(
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
      return "pk={} name={} distance={} magnitude={}".format(
      self.pk, self.name, self.distance, self.magnitude
      )



class Language(models.Model):
    '''
    Layout from http://www-01.sil.org/iso639-3/download.asp. The Django 
    string convention of empty string is used, not null=True. blank=True
    is used to indicate a possible empty value. 'scope' and 'type' 
    columns are defined with choices.
    '''
    id = models.CharField(
      db_index=True,
      max_length=3,
      primary_key=True,
      help_text="The three-letter 639-3 identifier.",
      )
      
    part2B = models.CharField(
      max_length=3,
      blank=True,
      help_text="Equivalent 639-2 identifier of the bibliographic applications code set, if there is one.",
      )
      
    part2T = models.CharField(
      max_length=3,
      blank=True,
      help_text="Equivalent 639-2 identifier of the terminology applications code set, if there is one.",
      )
      
    part1 = models.CharField(
      max_length=2,
      blank=True,
      help_text="Equivalent 639-1 identifier, if there is one.",
      )
      
    INDIVIDUAL = 'I'
    MACROLANGUAGE = 'M'
    SPECIAL = 'S'
    SCOPE_CHOICES = (
        (INDIVIDUAL, 'Individual'),
        (MACROLANGUAGE, 'Macrolanguage'),
        (SPECIAL, 'Special'),
    )
    scope = models.CharField(
      max_length=1,
      choices=SCOPE_CHOICES,
      help_text="I(ndividual), M(acrolanguage), S(pecial).",
      )

    ANCIENT = 'A'
    CONSTRUCTED = 'C'
    EXTINCT = 'E'
    HISTORICAL = 'H'
    LIVING = 'L'
    SPECIAL = 'S'
    TYPE_CHOICES = (
        (ANCIENT, 'Ancient'),
        (CONSTRUCTED, 'Constructed'),
        (EXTINCT, 'Extinct'),
        (HISTORICAL, 'Historical'),
        (LIVING, 'Living'),
        (SPECIAL, 'Special'),
        )      
    type = models.CharField(
      max_length=1,
      choices=TYPE_CHOICES,
      help_text="A(ncient), C(onstructed), E(xtinct), H(istorical), L(iving), S(pecial).",
      )
      
    name = models.CharField(
      "Reference name",
      max_length=150,
      help_text="Reference language name.",
      )
      
    comment = models.CharField(
      max_length=150,
      blank=True,
      help_text="Comment relating to one or more of the columns.",
      )
      
    def __str__(self):
      return "id='{}' part1='{}' scope='{}' type='{}' name='{}' comment='{}'".format(
      self.pk, self.part1, self.scope, self.type, self.name, self.comment
      )
