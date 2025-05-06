from django.urls import path
from .views import CountryListView, CountryDetailView

urlpatterns = [
    path('api/countries/', CountryListView.as_view(), name='country-list-create'),
    path('api/countries/<str:cca3>/', CountryDetailView.as_view(), name='country-detail'),

]