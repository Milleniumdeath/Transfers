
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
