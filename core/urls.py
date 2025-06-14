
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/',ClubInfoView.as_view(), name='club-info' ),
    path('latest-transfers', LatestTransfersView.as_view(), name='latest-transfers' ),
    path('players/', PlayersView.as_view(), name='players'),
    path('U_20_players/', U_20_PlayersView.as_view(), name='U_20_players'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('about/', AboutView.as_view(), name='about'),
]

urlpatterns += [
    path('stats/top-150-accurate-predictions/', Top150AccuratePredictionView.as_view(), name ='top-150'),
    path('stats/top-50-expenditure-clubs/', Top50expenditureclubsView.as_view(), name ='top-50'),
    path('stats/transfer-records/', TransfersRecordsView.as_view(), name ='records'),
    path('stats/top-50-clubs-by-income/', Top50incomeclubsView.as_view(), name='income50')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
