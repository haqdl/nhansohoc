from django.contrib import admin
from .models import (
    LifePath,
    DestinyPath,
    HearthDesire,
    Personality,
    PowerPath,
    ActivePath,
    LegacyPath,
    ExpressionPath
)

# Register your models here.
admin.site.register(LifePath)
admin.site.register(DestinyPath)
admin.site.register(HearthDesire)
admin.site.register(Personality)
admin.site.register(PowerPath)
admin.site.register(ActivePath)
admin.site.register(LegacyPath)
admin.site.register(ExpressionPath)
