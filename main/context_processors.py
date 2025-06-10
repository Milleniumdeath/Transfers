from django.db.models import Count

from .models import *

def get_countries(requeast):
    countries = Country.objects.annotate(club_count=Count('club')).filter(club_count__gt=0).order_by('-club_count')
    left_countries = list(countries)[::2]
    right_countries = list(countries)[1::2]

    context = {
        'countries': countries,
        'left_countries': left_countries,
        'right_countries': right_countries,

    }
    return context