from django.db import models
from django.forms import ValidationError
from localflavor.br.models import BRCPFField
from django.utils.translation import gettext_lazy as _
import phonenumbers


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = BRCPFField(_('CPF'), unique=True)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    def clean(self):
        try:
            # Converte o número de telefone em um objeto PhoneNumber
            phone_number = phonenumbers.parse(self.telefone, "BR")
            # Verifica se o número de telefone é válido
            if not phonenumbers.is_valid_number(phone_number):
                raise ValidationError("Número de telefone inválido.")
            # Formata o número de telefone para a forma internacional
            self.telefone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except phonenumbers.NumberParseException:
            raise ValidationError("Número de telefone inválido.")