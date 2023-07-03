from rest_framework import generics
from .models import Club 
from .serializers import ClubSerializer

# Create your views here.

# ListAPIView
class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer