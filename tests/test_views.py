from unittest.mock import Mock

from django.test import TestCase, override_settings

from ..views import DefaultForward, IncomingCallCreate


class DefaultForwardTest(TestCase):

    @override_settings(TWILIO_DEFAULT_FORWARD_NO="+13862229998")
    def test_post(self):
        # setup
        view = DefaultForward()
        view.twilio_request = Mock(to="+13862229999")
        response = view.post("")

        # asserts
        self.assertEqual(
            response.__str__(),
            ('<?xml version="1.0" encoding="UTF-8"?><Response><Dial '
                'callerId="+13862229999">+13862229998</Dial></Response>')
        )


class IncomingCallCreateTest(TestCase):

    def test_get_form_kwargs(self):
        # setup
        view = IncomingCallCreate()
        view.twilio_request = Mock(to="+13862229999", from_="+13862229998")

        # asserts
        self.assertDictEqual(
            view.get_form_kwargs(),
            {
                "data": {
                    "to_number": "+13862229999", "from_number": "+13862229998"
                }
            }
        )

    @override_settings(TWILIO_DEFAULT_FORWARD_NO="+13862229998")
    def test_form_valid(self):
        # setup
        form = Mock()
        view = IncomingCallCreate()
        view.twilio_request = Mock(to="+13862229999")
        response = view.form_valid(form)

        # asserts
        self.assertEqual(
            response.__str__(),
            ('<?xml version="1.0" encoding="UTF-8"?><Response><Dial '
                'callerId="+13862229999">+13862229998</Dial></Response>')
        )
        form.save.assert_called_once()
