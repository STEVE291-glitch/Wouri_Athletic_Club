from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from .models import Match

from .models import (
    Club,
    Joueur,
    Match,
    Actualite,
    Media,
    MessageContact,
    Abonne,
    CarteAbonnement,
    InscriptionAbonnement,
    # Partenaire  # ← décommente SEULEMENT si le modèle existe
)

# ===========================
# Pages simples
# ===========================

def accueil(request):
    return render(request, 'football_app/index.html')


def club(request):
    return render(request, 'football_app/club.html')


def effectif(request):
    joueurs = Joueur.objects.all()
    return render(request, 'football_app/effectif.html', {'joueurs': joueurs})


def matchs(request):
    matchs = Match.objects.all()
    return render(request, 'football_app/matchs.html', {'matchs': matchs})


def actualites(request):
    actualites = Actualite.objects.all()
    return render(request, 'football_app/actualites.html', {'actualites': actualites})


def galerie(request):
    medias = Media.objects.all()
    return render(request, 'football_app/galerie.html', {'medias': medias})


def contact(request):
    if request.method == 'POST':
        MessageContact.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            sujet=request.POST.get('sujet'),
            message=request.POST.get('message'),
        )
    return render(request, 'football_app/contact.html')


# ===========================
# Abonnements
# ===========================

def carte_abonnement(request):
    cartes = CarteAbonnement.objects.filter(actif=True)

    if request.method == 'POST':
        abonne = Abonne.objects.create(
            prenom=request.POST.get('prenom'),
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            whatsapp=request.POST.get('whatsapp'),
        )

        carte = CarteAbonnement.objects.get(id=request.POST.get('carte_id'))

        InscriptionAbonnement.objects.create(
            abonne=abonne,
            carte=carte
        )

        send_mail(
            subject="📩 Nouvelle demande d’abonnement",
            message=(
                f"Nouvelle inscription :\n\n"
                f"Nom : {abonne.prenom} {abonne.nom}\n"
                f"Email : {abonne.email}\n"
                f"WhatsApp : {abonne.whatsapp}\n"
                f"Carte : {carte.nom}\n"
                f"Prix : {carte.prix} FCFA"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=True,
        )

        return redirect('carte_abonnement')

    return render(request, 'football_app/carte_abonnement.html', {
        'cartes': cartes
    })


# ===========================
# Partenaires
# ===========================

def partenaires(request):
    return render(request, 'football_app/partenaires.html')

def prochain_match(request):
    maintenant = timezone.now()

    prochain_match = (
        Match.objects
        .filter(date_heure__gte=maintenant)
        .order_by('date_heure')
        .first()
    )

    return render(request, 'football_app/prochain_match.html', {
        'prochain_match': prochain_match
    })
