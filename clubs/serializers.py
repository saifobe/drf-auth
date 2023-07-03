from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model=Club
        fields = ('id', 'fan', 'name', 'club_wiki', 'created_at', 'updated_at')