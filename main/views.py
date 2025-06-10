from django.shortcuts import render, get_object_or_404



from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()

        country = request.GET.get('country')
        if country is not None:
            clubs = clubs.filter(country__id=country)

        context = {
            'clubs': clubs
        }
        return render(request, 'clubs.html', context)


class ClubInfoView(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, id=pk)
        players = club.player_set.order_by('-price')
        context = {
            'club': club,
            'players': players
        }
        return render(request, 'clubs-info.html', context)

class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.filter(season=Season.objects.last()).order_by('-price')
        context = {
            'transfers': transfers,
        }
        return render(request, 'latest-transfers.html', context)

class PlayersView(View):
    def get(self, request):
        return render(request, 'players.html')

class U_20_PlayersView(View):
    def get(self, request):
        return render(request, 'U_20_players.html')

class TryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html')

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')