from django.contrib import admin

# Register your models here.
from geo_api.models import Polygon, LineString, Point

from django.contrib.gis.admin import ModelAdmin as GeoModelAdmin

admin.site.register(Point)
admin.site.register(Polygon)
admin.site.register(LineString)
# admin.site.register(City)
# admin.site.register(City)
# class PolygonAdmin(admin.ModelAdmin):
#     pass
#
# admin.register(LineString)
#
# from django.contrib import admin



class PointAdmin(GeoModelAdmin):
    # list_display = ('name', 'geometry')
    pass


class SSSAdmin(admin.ModelAdmin):
    # list_display = ('name', 'geometry')
    pass

# admin.register(Point, PointAdmin)
# admin.register(SSS,SSSAdmin)
