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
    
    male_features = ['athletic', 'fat', 'handsome', 'hot', 'fit', 'clean-cut',
                'sexy', 'sculpted', 'confident', 'jockey', 'smart',
                'stylish', 'suave', 'macho', 'masculine', 'manly', 
                'bold', 'youthful', 'brash']
    
    female_features = ['beautiful', 'cute', 'elegant', 'glamorous', 'classy', 
                  'foxy', 'sexy', 'athletic', 'chic', 'modern', 'barbie',
                  'attractive', 'fashionable', 'glossy', 'goddess',
                  'glowing', 'hot', 'lovely', 'prim', 'sharp']   
