from django.db import models

# Create your models here.


class LifePath(models.Model):
    life_path_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True)
    meaning = models.TextField(blank=True)
    
    def __str__(self):
        return self.meaning


class DestinyPath(models.Model):
    destiny_path_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True)
    meaning = models.TextField(blank=True)    

    def __str__(self):
        return self.meaning


class HearthDesire(models.Model):
    hearth_desire_number = models.IntegerField(primary_key=True ,unique=True)    
    description = models.TextField(blank=True)
    meaning = models.TextField(blank=True)

    def __str__(self):
        return self.meaning

class Personality(models.Model):
    personality_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True) 
    meaning = models.TextField(blank=True)       

    def __str__(self):
        return self.meaning


class PowerPath(models.Model):
    power_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True)
    meaning = models.TextField(blank=True)    

    def __str__(self):
        return self.meaning


class ActivePath(models.Model):
    active_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True) 
    meaning = models.TextField(blank=True)    

    def __str__(self):
        return self.meaning


class LegacyPath(models.Model):
    legacy_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True) 
    meaning = models.TextField(blank=True)    

    def __str__(self):
        return self.meaning


class ExpressionPath(models.Model):
    expression_number = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField(blank=True) 
    meaning = models.TextField(blank=True)    

    def __str__(self):
        return self.meaning
