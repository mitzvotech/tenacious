from app.models import Client, Bundle, Document
from rest_framework import serializers

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email_address')

class BundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bundle
        # fields = ('first_name', 'last_name', 'email_address')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        # fields = ('first_name', 'last_name', 'email_address')