from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class MeaningModel(models.Model):
    model_number = models.IntegerField(primary_key=True, unique=True)
    key_info = models.CharField(max_length=200)
    description = RichTextField()
    meaning = RichTextField()

    def __str__(self):
        return self.key_info
        
    class Meta:
        abstract = True

class LifePath(MeaningModel):   
    class Meta:    
        verbose_name = 'SỐ CHỦ ĐẠO'
        verbose_name_plural = 'CHỈ SỐ CHỦ ĐẠO'


class DestinyPath(MeaningModel):
    class Meta:    
        verbose_name = 'SỨ MỆNH'
        verbose_name_plural = 'CHỈ SỐ SỨ MỆNH'


class HearthDesire(MeaningModel):
    class Meta:    
        verbose_name = 'LINH HỒN'
        verbose_name_plural = 'CHỈ SỐ LINH HỒN'     


class Personality(MeaningModel):
    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'NHÂN CÁCH'
        verbose_name_plural = 'CHỈ SỐ NHÂN CÁCH'   


class PowerPath(MeaningModel):
    class Meta:    
        verbose_name = 'SỐ TRƯỞNG THÀNH'
        verbose_name_plural = 'CHỈ SỐ TRƯỞNG THÀNH' 


class ActivePath(MeaningModel):
    class Meta:    
        verbose_name = 'TÊN HIỆN TẠI'
        verbose_name_plural = 'CHỈ SỐ TÊN HIỆN TẠI' 


class LegacyPath(MeaningModel):
    class Meta:    
        verbose_name = 'Legac'
        verbose_name_plural = 'Legacy Path' 

class ExpressionPath(MeaningModel):
    class Meta:    
        verbose_name = 'Expression '
        verbose_name_plural = 'Expression Path' 
