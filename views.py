from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, View

from django_twilio.decorators import twilio_view
from django_twilio.request import decompose
from twilio.twiml.voice_response import VoiceResponse

from .forms import IncomingCallForm
from .models import IncomingCall


class TwilioView(View):

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        self.twilio_request = decompose(request)
        return super().dispatch(request, *args, **kwargs)


class DefaultForward(TwilioView):

    http_method_names = ["post",]

    def post(self, request, *args, **kwargs):
        response = VoiceResponse()
        response.dial(
            caller_id=self.twilio_request.to,
            number=settings.TWILIO_DEFAULT_FORWARD_NO
        )
        return response


class IncomingCallCreate(CreateView, TwilioView):

    form_class = IncomingCallForm
    model = IncomingCall

    def get_form_kwargs(self):
        return {
            "data": {
                "to_number": self.twilio_request.to,
                "from_number": self.twilio_request.from_
            }
        }

    def form_valid(self, form):
        form.save()
        response = VoiceResponse()
        response.dial(
            caller_id=self.twilio_request.to,
            number=settings.TWILIO_DEFAULT_FORWARD_NO
        )
        return response
