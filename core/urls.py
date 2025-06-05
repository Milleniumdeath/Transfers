
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
    path('latest-transfers', LatestTransfersView.as_view(), name='latest-transfers' )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
