from django.urls import path

from calls import views

app_name = "calls"
urlpatterns = [
    path("default-forward/", views.DefaultForward.as_view(), name="default_forward"),
    path("incoming-calls/create/", views.IncomingCallCreate.as_view(), name="incoming_call_create"),
]
