from django.urls import path
from .views import CountryListCreateView, CountryDetailUpdateDeleteView

urlpatterns = [
    path('api/countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('api/countries/<str:cca3>/', CountryDetailUpdateDeleteView.as_view(), name='country-detail'),

]