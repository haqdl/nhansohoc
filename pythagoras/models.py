from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class MeaningModel(models.Model):
    model_number = models.IntegerField(primary_key=True, unique=True)
    key_info = models.CharField(max_length=200, null=True, default='')
    description = RichTextField()
    meaning = RichTextField()

    def __str__(self):
        return f'{self.model_number} - {self.key_info}'

    def to_dict(self):
        out_dict = {
            "model_number": self.model_number,
            "key_info": self.key_info,
            "description": self.description,
            "meaning": self.meaning,
        }
        return out_dict
        
    class Meta:
        abstract = True

class LifePath(MeaningModel):   
    class Meta:    
        verbose_name = 'SỐ ĐƯỜNG ĐỜI'
        verbose_name_plural = 'CHỈ SỐ ĐƯỜNG ĐỜI'


class DestinyPath(MeaningModel):
    class Meta:    
        verbose_name = 'SỨ MỆNH'
        verbose_name_plural = 'CHỈ SỐ SỨ MỆNH'


class HearthDesire(MeaningModel):
    class Meta:    
        verbose_name = 'SỐ ĐỘNG LỰC'
        verbose_name_plural = 'CHỈ SỐ ĐỘNG LỰC'     


class Personality(MeaningModel):
    def __str__(self):
        return self.meaning

    class Meta:    
        verbose_name = 'TÍNH CÁCH'
        verbose_name_plural = 'CHỈ SỐ TÍNH CÁCH'   


class PowerPath(MeaningModel):
    class Meta:    
        verbose_name = 'THÀNH TỰU'
        verbose_name_plural = 'CHỈ SỐ THÀNH TỰU' 


class AttitudePath(MeaningModel):
    class Meta:    
        verbose_name = 'SỐ THÁI ĐỘ'
        verbose_name_plural = 'CHỈ SỐ THÁI ĐỘ' 


class PassionPath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ ĐAM MÊ'
        verbose_name_plural = 'CHỈ SỐ ĐAM MÊ' 


class ChallengePath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ THÁCH THỨC'
        verbose_name_plural = 'CHỈ SỐ THÁCH THỨC' 


class MissingPath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ THIẾU'
        verbose_name_plural = 'CHỈ SỐ RÈN LUYỆN' 


class PyramidPath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ CHẶNG'
        verbose_name_plural = '4 ĐỈNH CAO CUỘC ĐỜI' 


class CyclePath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ CHU KỲ'
        verbose_name_plural = '3 GIAI ĐOẠN CỦA CUỘC ĐỜI' 

class BirthdayDayPath(MeaningModel):
    class Meta:    
        verbose_name = 'CHỈ SỐ NGÀY SINH'
        verbose_name_plural = 'CHỈ SỐ NGÀY SINH' 


class BirthdayMonthPath(MeaningModel):
    class Meta:    
        verbose_name = 'THÁNG CÁ NHÂN'
        verbose_name_plural = 'CHỈ SỐ THÁNG CÁ NHÂN'    


class BirthdayYearPath(MeaningModel):
    class Meta:    
        verbose_name = 'NĂM CÁ NHÂN'
        verbose_name_plural = 'CHỈ SỐ NĂM CÁ NHÂN' 

             
class ActivePath(MeaningModel):
    class Meta:    
        verbose_name = 'TÊN HIỆN TẠI'
        verbose_name_plural = 'CHỈ SỐ TÊN HIỆN TẠI' 


class LegacyPath(MeaningModel):
    class Meta:    
        verbose_name = 'HỌ HIỆN TẠI'
        verbose_name_plural = 'CHỈ SỐ HỌ HIỆN TẠI' 

