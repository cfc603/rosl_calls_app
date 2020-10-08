from django.test import TestCase

from ..forms import IncomingCallForm
from ..models import IncomingCall, PhoneNumber


class IncomingCallFormTest(TestCase):

    def test_save(self):
        # setup
        form = IncomingCallForm(
            data={"to_number": "+12125552368", "from_number": "+12125552368"}
        )
        form.is_valid()
        call = form.save()
        phone_number = PhoneNumber.objects.first()

        # asserts
        self.assertEqual(IncomingCall.objects.count(), 1)
        self.assertEqual(PhoneNumber.objects.count(), 1)
        self.assertEqual(call.to_number, phone_number)
        self.assertEqual(call.from_number, phone_number)
