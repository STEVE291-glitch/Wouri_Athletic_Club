from django.test import TestCase
from .models import Club, Joueur, Match

# ===========================
# ✅ Tests unitaires de base
# ===========================

class ClubModelTest(TestCase):
    def setUp(self):
        self.club = Club.objects.create(
            nom="FC Django",
            slogan="Le code, notre passion",
            histoire="Un club né pour le football numérique."
        )

    def test_club_creation(self):
        self.assertEqual(self.club.nom, "FC Django")
        self.assertEqual(str(self.club), "FC Django")


class JoueurModelTest(TestCase):
    def setUp(self):
        self.club = Club.objects.create(nom="FC Django")
        self.joueur = Joueur.objects.create(
            nom="Émile Nkwei",
            poste="Attaquant",
            numero=9,
            age=22,
            club=self.club
        )

    def test_joueur_creation(self):
        self.assertEqual(self.joueur.nom, "Émile Nkwei")
        self.assertEqual(str(self.joueur), "Émile Nkwei (Attaquant)")
        self.assertEqual(self.joueur.club.nom, "FC Django")


class MatchModelTest(TestCase):
    def setUp(self):
        self.club = Club.objects.create(nom="FC Django")
        self.match = Match.objects.create(
            adversaire="Real Python",
            date="2025-11-10",
            lieu="Stade Django",
            competition="Championnat",
            score_domicile=3,
            score_exterieur=1,
            club=self.club
        )

    def test_match_creation(self):
        self.assertEqual(str(self.match), "FC Django vs Real Python (2025-11-10)")
        self.assertEqual(self.match.score_domicile, 3)

