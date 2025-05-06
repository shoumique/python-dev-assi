from rest_framework import generics, filters
from .models import Country
from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class CountryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'cca3'

class SameRegionCountriesView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, region):
        countries = Country.objects.filter(region__iexact=region)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    
class SameLanguageCountriesView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, language_code):
        countries = Country.objects.filter(languages__has_key=language_code)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    
class CountrySearchView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_common', 'name_official']

    def get_queryset(self):
        return Country.objects.all()
        



@login_required
def country_list(request):
    query = request.GET.get('q')
    if query:
        countries = Country.objects.filter(name_common__icontains=query)
    else:
        countries = Country.objects.all()
    return render(request, 'countries/country_list.html', {'countries': countries})


@login_required
def country_detail(request, country_id):
    country = Country.objects.get(id=country_id)
    same_region = Country.objects.filter(region=country.region).exclude(id=country.id)
    languages = country.languages.values() if isinstance(country.languages, dict) else []

    print(same_region)
    print(languages)

    return render(request, 'countries/country_detail.html', {
        'country': country,
        'same_region': same_region,
        'languages': languages
    })
