from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from .models import Rendezvous
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Personnalisation ou suppression des messages d'erreur
        self.fields["password1"].help_text = None  # Supprime l'aide sur le mot de passe
        self.fields[
            "password2"
        ].help_text = None  # Supprime l'aide sur le champ de confirmation
        self.fields[
            "username"
        ].help_text = None 

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["name", "phone_number", "email", "ticket_quantity", "message"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.startswith("+225"):
            phone_number = "+225" + phone_number.lstrip("0")
        return phone_number


class CommandeForm(forms.Form):
    nom = forms.CharField(label="Nom et Prénoms", max_length=100)
    quantite = forms.IntegerField(label="Quantité", min_value=1)
    numero = forms.CharField(label="Numéro de téléphone", max_length=20)
    lieu_livraison = forms.CharField(label="Lieu de livraison", max_length=200)


class RendezVousForm(forms.ModelForm):
    class Meta:
        model = Rendezvous
        fields = [
            "nom",
            "email",
            "phone",
            "date",
            "heure",
            "message",
            "service",
            "tarif",
        ]

        widgets = {
            "service": forms.TextInput(attrs={"readonly": "readonly"}),
            "tarif": forms.TextInput(attrs={"readonly": "readonly"}),
        }
