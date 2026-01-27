from django.db import models

# ===========================
# 1️⃣  Modèle du club
# ===========================
class Club(models.Model):
    nom = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200, blank=True)
    histoire = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    date_creation = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nom


# ===========================
# 2️⃣  Staff (dirigeants, entraîneurs, etc.)
# ===========================
class Staff(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='staff')

    def __str__(self):
        return f"{self.nom} - {self.poste}"


# ===========================
# 3️⃣  Joueurs
# ===========================
class Joueur(models.Model):
    PIED_CHOICES = [
        ('droit', 'Droit'),
        ('gauche', 'Gauche'),
        ('ambi', 'Ambidextre'),
    ]

    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=50)
    numero = models.PositiveIntegerField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    nationalite = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='joueurs/', blank=True, null=True)

    pied_fort = models.CharField(
        max_length=10,
        choices=PIED_CHOICES,
        blank=True
    )
    taille = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Taille en mètres (ex: 1.75)"
    )
    poids = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Poids en kg"
    )

    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='joueurs')

    buts = models.PositiveIntegerField(default=0)
    passes = models.PositiveIntegerField(default=0)
    cartons_jaunes = models.PositiveIntegerField(default=0)
    cartons_rouges = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nom} ({self.poste})"


# ===========================
# 4️⃣  Matchs
# ===========================
class Match(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    adversaire = models.CharField(max_length=100)
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=100)
    competition = models.CharField(max_length=100)
    score_domicile = models.IntegerField(null=True, blank=True)
    score_exterieur = models.IntegerField(null=True, blank=True)
    resume = models.TextField(blank=True)
def __str__(self):
    return f"{self.club} vs {self.adversaire} - {self.date_heure}"
    
    



# ===========================
# 5️⃣  Actualités
# ===========================
class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualites/', blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_publication']


# ===========================
# 6️⃣  Galerie (photos / vidéos)
# ===========================
class Media(models.Model):
    TYPE_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Vidéo'),
    ]
    titre = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='media/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} ({self.type})"


# ===========================
# 7️⃣  Messages de contact
# ===========================
class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom} ({self.email})"
class Abonne(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField(blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class CarteAbonnement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree_mois = models.IntegerField()
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

# ===========================
# 8️⃣  Inscription abonnement
# ===========================
class InscriptionAbonnement(models.Model):
    abonne = models.ForeignKey(
        Abonne,
        on_delete=models.CASCADE
    )
    carte = models.ForeignKey(
        CarteAbonnement,
        on_delete=models.CASCADE,
        related_name='inscriptions'
    )
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('valide', 'Validé'),
            ('rejete', 'Rejeté'),
        ],
        default='en_attente'
    )

    def __str__(self):
        return f"{self.abonne} - {self.carte.nom}"

class Partenaire(models.Model):
    nom = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='partenaires/')
    site_web = models.URLField(blank=True, null=True)
    actif = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
