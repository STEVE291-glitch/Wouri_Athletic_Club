from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('club/', views.club, name='club'),
    path('effectif/', views.effectif, name='effectif'),
    path('matchs/', views.matchs, name='matchs'),
    path('actualites/', views.actualites, name='actualites'),
    path('galerie/', views.galerie, name='galerie'),
    path('contact/', views.contact, name='contact'),

    path('abonnements/', views.carte_abonnement, name='carte_abonnement'),
    path('partenaires/', views.partenaires, name='partenaires'),
    path('prochain-match/', views.prochain_match, name='prochain_match'),
]
