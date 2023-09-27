from rest_framework import serializers

from .models import *

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog 
        fields = ('id', 'title', 'content')