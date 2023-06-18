from django.urls import path

from . import views

urlpatterns = [
    # /analyze/account
    path("account/", views.get_account_CLIP_result, name="get_account_CLIP_result"),
    
    # /analyze/image
    path("image/", views.get_img_CLIP_result, name="get_img_CLIP_result"),
    
    # /analyze/images
    path("images/", views.get_imgs_CLIP_result, name="get_imgs_CLIP_result")
]