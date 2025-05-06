from django.urls import path
from .views import (
    CountryListCreateView,
    CountryDetailUpdateDeleteView,
    SameRegionCountriesView,
    SameLanguageCountriesView,
    CountrySearchView,
    country_list,
    country_detail
)

urlpatterns = [
    path('api/countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('api/countries/search/', CountrySearchView.as_view(), name='country-search'),
    path('api/countries/region/<str:region>/', SameRegionCountriesView.as_view(), name='same-region-countries'),
    path('api/countries/language/<str:language_code>/', SameLanguageCountriesView.as_view(), name='same-language-countries'),
    path('api/countries/<str:cca3>/', CountryDetailUpdateDeleteView.as_view(), name='country-detail'),

    path('web/', country_list, name='country_list'),
    path('web/<int:country_id>/', country_detail, name='country_detail'),
]