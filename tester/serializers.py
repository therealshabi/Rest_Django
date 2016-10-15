from rest_framework import serializers

from tester.models import Details


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ['name',]
