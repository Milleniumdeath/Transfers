from django.shortcuts import render, get_object_or_404



from django.views import View
from .models import *
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
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