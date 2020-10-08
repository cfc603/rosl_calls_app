from django import forms

from phonenumber_field.formfields import PhoneNumberField

from .models import IncomingCall, PhoneNumber


class IncomingCallForm(forms.Form):

    to_number = PhoneNumberField()
    from_number = PhoneNumberField()

    def save(self, commit=True):
        return IncomingCall.objects.create(
            to_number=PhoneNumber.objects.get_or_create(
                number=self.cleaned_data["to_number"],
                defaults={"name": self.cleaned_data["to_number"]}
            )[0],
            from_number=PhoneNumber.objects.get_or_create(
                number=self.cleaned_data["from_number"],
                defaults={"name": self.cleaned_data["from_number"]}
            )[0],
        )
