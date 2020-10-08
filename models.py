from django.db import models

from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class IncomingCall(TimeStampedModel):

    to_number = models.ForeignKey(
        "PhoneNumber", on_delete=models.PROTECT, related_name="to_numbers"
    )
    from_number = models.ForeignKey(
        "PhoneNumber", on_delete=models.PROTECT, related_name="from_numbers"
    )

    def __str__(self):
        return f"Incoming call from {self.from_number.name} to {self.to_number.name}"


class PhoneNumber(models.Model):

    name = models.CharField(max_length=120)
    number  = PhoneNumberField(unique=True)

    def __str__(self):
        return self.name
