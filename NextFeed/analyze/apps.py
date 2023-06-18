from django.apps import AppConfig
from PIL import Image
import torch
import urllib
import requests
from transformers import CLIPProcessor, CLIPModel

class AnalyzeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analyze'
    
    CLIP_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
    CLIP_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")
    
    male_features = ['handsome', 'fit', 'clean',
                'sexy', 'sculpted', 'classy',
                'stylish', 'suave', 'macho', 'dandy']
    
    female_features = ['beautiful', 'adorable', 'elegant', 'glamorous', 
                  'athletic', 'attractive', 'fashionable', 'goddess',
                  'lovely', 'prim', 'pure']   
