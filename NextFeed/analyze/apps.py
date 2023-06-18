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
    
    male_features = ['athletic', 'fat', 'handsome', 'fit', 'clean',
                'sexy', 'sculpted', 'confident', 'jokey', 'smart',
                'stylish', 'suave', 'macho', 'manly', 
                'bold', 'youthful']
    
    female_features = ['beautiful', 'cute', 'elegant', 'glamorous', 'classy', 
                  'foxy', 'sexy', 'athletic', 'barbie',
                  'attractive', 'fashionable', 'goddess',
                  'glowing', 'lovely', 'prim', 'sharp', 'pure']   
