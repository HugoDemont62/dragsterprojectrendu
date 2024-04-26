from django.urls import path, include
from .views import authView, home, regleView, classementView, place_bet, check_bet

urlpatterns = [
    path("", home, name="home"),
    path("regle/", regleView, name="relge"),
    path("classement/", classementView, name="classement"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('place_bet/', place_bet, name='place_bet'),
    path('check_bet/', check_bet, name='check_bet'),
]
