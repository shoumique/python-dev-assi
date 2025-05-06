from django.urls import path
from .views import CountryListCreateView, CountryDetailUpdateDeleteView, SameRegionCountriesView

urlpatterns = [
    path('api/countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('api/countries/<str:cca3>/', CountryDetailUpdateDeleteView.as_view(), name='country-detail'),
    path('api/countries/region/<str:region>/', SameRegionCountriesView.as_view(), name='same-region-countries'),

]