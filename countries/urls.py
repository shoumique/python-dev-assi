from django.urls import path
from .views import CountryListCreateView, CountryDetailUpdateView

urlpatterns = [
    path('api/countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('api/countries/<str:cca3>/', CountryDetailUpdateView.as_view(), name='country-detail'),

]