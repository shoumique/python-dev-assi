from django.db import models

class Country(models.Model):
    name_common = models.CharField(max_length=255)
    name_official = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=2)
    cca3 = models.CharField(max_length=3, unique=True)
    ccn3 = models.CharField(max_length=3)
    cioc = models.CharField(max_length=3)
    flag = models.URLField()
    capital = models.CharField(max_length=255)
    area = models.IntegerField()
    population = models.IntegerField()
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)
    languages = models.JSONField()  # Store language data (e.g., {'eng': 'English', 'tsn': 'Tswana'})
    latlng = models.JSONField()  # Store lat and lng as a list (e.g., [-22, 24])
    landlocked = models.BooleanField()
    borders = models.JSONField()  # List of border country codes (e.g., ['NAM', 'ZAF'])
    currency = models.JSONField()  # Store currency data (e.g., {'BWP': {'symbol': 'P', 'name': 'Botswana pula'}})
    timezones = models.JSONField()
    fifa = models.CharField(max_length=3, blank=True, null=True)
    gini = models.JSONField(blank=True, null=True)  # Store Gini coefficient if available
    coat_of_arms = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name_common
