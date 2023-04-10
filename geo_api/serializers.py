from rest_framework import serializers, filters
from rest_framework.fields import CharField

from geo_api.models import Polygon, LineString, Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer



class PolygonSerializer(GeoFeatureModelSerializer):
    points = serializers.StringRelatedField(many=True)
    class Meta:
        model = Polygon
        geo_field = 'geometry'
        fields = ["name", "geometry",'points', 'id']
        # fields = "__all__"

class LineStringSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LineString
        geo_field = 'geometry'
        fields = ["name", "geometry"]

class PointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Point
        # filterset_fields = ['name']
        filter_backends = [filters.SearchFilter]
        search_fields = ['name', ]
        geo_field = 'geometry'
        fields = ["name", "geometry"]



from rest_framework.serializers import Serializer, FileField


def required_custom(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField(required=True)
    name = CharField(validators=[required_custom])
    geom_type = serializers.CharField()
    class Meta:
        fields = ['file_uploaded','name','geom_type']

#
#     """ A class to serialize locations as GeoJSON compatible data """
#
#     class Meta:
#         # model = School
#         # geo_field = 'location'
#         # auto_bbox = True
        #
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        # fields = ('id', 'name', 'county', 'enrollment', 'location', 'electricity_availability', 'emmis_code')


# from drf_extra_fields.geo_fields import PointField
#
# class PointSerializer(serializers.ModelSerializer):
#     geometry = PointField()
#
#     class Meta:
#         model = Point
#         fields = ('geometry')

# class PointSerializer(GeoFeatureModelSerializer):
#
#     class Meta:
#         model = Point
#         fields = ('geometry')
#         id_field = False
#         # fields = settings.FEATURE_FIELDS_TO_SERIALIZE
#         geo_field = "geometry"


