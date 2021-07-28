from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class LifePath(models.Model):
    life_path_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField()
    meaning = RichTextField()
    
    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'SỐ CHỦ ĐẠO'
        verbose_name_plural = 'CHỈ SỐ CHỦ ĐẠO'


class DestinyPath(models.Model):
    destiny_path_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField()
    meaning = RichTextField()    

    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'SỨ MỆNH'
        verbose_name_plural = 'CHỈ SỐ SỨ MỆNH'


class HearthDesire(models.Model):
    hearth_desire_number = models.IntegerField(primary_key=True ,unique=True)    
    description = RichTextField()
    meaning = RichTextField()

    def __str__(self):
        return self.meaning
    
    class Meta:    
        verbose_name = 'LINH HỒN'
        verbose_name_plural = 'CHỈ SỐ LINH HỒN'     


class Personality(models.Model):
    personality_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField() 
    meaning = RichTextField()       

    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'NHÂN CÁCH'
        verbose_name_plural = 'CHỈ SỐ NHÂN CÁCH'   


class PowerPath(models.Model):
    power_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField()
    meaning = RichTextField()    

    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'SỐ TRƯỞNG THÀNH'
        verbose_name_plural = 'CHỈ SỐ TRƯỞNG THÀNH' 


class ActivePath(models.Model):
    active_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField() 
    meaning = RichTextField()    

    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'TÊN HIỆN TẠI'
        verbose_name_plural = 'CHỈ SỐ TÊN HIỆN TẠI' 


class LegacyPath(models.Model):
    legacy_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField() 
    meaning = RichTextField()    

    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'Legacy Path'
        verbose_name_plural = 'Legacy Path' 

class ExpressionPath(models.Model):
    expression_number = models.IntegerField(primary_key=True, unique=True)
    description = RichTextField() 
    meaning = RichTextField()    

    def __str__(self):
        return self.meaning
