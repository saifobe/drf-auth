from django.urls import path
from .views import ClubList, ClubDetail



urlpatterns = [
    path('', ClubList.as_view(), name='club_list'),
    path('<int:pk>/', ClubDetail.as_view(), name='club_detail'),
]