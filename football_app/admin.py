from django.contrib import admin
from .models import (
    Club,
    Staff,
    Joueur,
    Match,
    Actualite,
    Media,
    MessageContact,
    Abonne,
    CarteAbonnement,
    InscriptionAbonnement,
    Partenaire
)

# ===========================
# CLUB
# ===========================
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_creation')
    search_fields = ('nom',)


# ===========================
# STAFF
# ===========================
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'club')
    list_filter = ('poste', 'club')
    search_fields = ('nom',)


# ===========================
# JOUEURS
# ===========================
@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'numero', 'club')
    list_filter = ('poste', 'club')
    search_fields = ('nom',)
    ordering = ('numero',)


# ===========================
# MATCHS ✅ CORRIGÉ DÉFINITIF
# ===========================
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'club',
        'adversaire',
        'date_heure',
        'lieu',
        'competition'
    )
    list_filter = ('club', 'competition')
    ordering = ('date_heure',)


# ===========================
# ACTUALITÉS
# ===========================
@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    ordering = ('-date_publication',)


# ===========================
# MÉDIAS
# ===========================
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('titre', 'type', 'date_ajout')
    list_filter = ('type',)


# ===========================
# CONTACT
# ===========================
@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi')


# ===========================
# ABONNÉS
# ===========================
@admin.register(Abonne)
class AbonneAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom')


# ===========================
# CARTES ABONNEMENT
# ===========================
@admin.register(CarteAbonnement)
class CarteAbonnementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'duree_mois', 'actif')


# ===========================
# INSCRIPTIONS
# ===========================
@admin.register(InscriptionAbonnement)
class InscriptionAbonnementAdmin(admin.ModelAdmin):
    list_display = (
        'abonne',
        'carte',
        'statut',
        'date_inscription'
    )


# ===========================
# PARTENAIRES
# ===========================
@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'actif', 'date_ajout')
