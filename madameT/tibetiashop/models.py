from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import random
import string
from django.contrib.auth.models import User
class Ticket(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14, unique=True)  # format +225XXXXXXXXXX
    email = models.EmailField()
    ticket_quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    available_tickets = models.PositiveIntegerField(default=200)
    

    def __str__(self):
        return f"Ticket for {self.name} - {self.ticket_quantity} tickets"
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/')
    description = models.TextField()
    code = models.CharField(max_length=6, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Commande(models.Model):
    STATUT_CHOICES = [
        ('Contacter', 'Contacter'),
        ('En cours', 'En cours'),
        ('Livré', 'Livré'),
    ]

    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    numero = models.CharField(max_length=15)
    quantite = models.IntegerField()
    lieu_livraison = models.CharField(max_length=255)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    code_produit = models.CharField(max_length=6, blank=True, null=True)
    nom_produit = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUT_CHOICES, default='Contacter')

    def __str__(self):
        return f"Commande {self.id} - {self.produit.nom}"
class Rendezvous(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    heure = models.TimeField()
    message = models.TextField(blank=True, null=True)
    service = models.CharField(max_length=100)
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("La date du rendez-vous ne peut pas être dans le passé.")

    def __str__(self):
        return f"{self.nom} - {self.date} {self.heure}"
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name} - {self.email}'
