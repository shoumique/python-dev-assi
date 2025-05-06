from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'cca3'

class SameRegionCountriesView(APIView):
    def get(self, request, region):
        countries = Country.objects.filter(region__iexact=region)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    
class SameLanguageCountriesView(APIView):
    def get(self, request, language_code):
        countries = Country.objects.filter(languages__has_key=language_code)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    