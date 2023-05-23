from django.urls import path

from . import views

urlpatterns = [
    # /analyze/account
    path("account/", views.get_account_CLIP_result, name="get_account_CLIP_result"),
]