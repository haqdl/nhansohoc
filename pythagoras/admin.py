from django.contrib import admin
from .models import (
    LifePath,
    DestinyPath,
    HearthDesire,
    Personality,
    PowerPath,
    ActivePath,
    LegacyPath,
    AttitudePath,
    PassionPath,
    ChallengePath,
    MissingPath,
    PyramidPath,
    CyclePath,
    BirthdayDayPath,
    BirthdayMonthPath,
    BirthdayYearPath,
    ActivePath,
    LegacyPath
)

# Register your models here.
admin.site.register(LifePath)
admin.site.register(DestinyPath)
admin.site.register(HearthDesire)
admin.site.register(Personality)
admin.site.register(PowerPath)
admin.site.register(AttitudePath)
admin.site.register(PassionPath)
admin.site.register(ChallengePath)
admin.site.register(MissingPath)
admin.site.register(PyramidPath)
admin.site.register(CyclePath)
admin.site.register(BirthdayDayPath)
admin.site.register(BirthdayMonthPath)
admin.site.register(BirthdayYearPath)
admin.site.register(ActivePath)
admin.site.register(LegacyPath)
