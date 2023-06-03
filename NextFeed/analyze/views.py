from django.shortcuts import render
from django.http import HttpResponse
import json
from PIL import Image
import requests
import torch
import math

import base64
import io

from .apps import AnalyzeConfig

def index(request):
    return HttpResponse("Hello, world")

def CLIP_result_one_img(imgbase64, usertype):
    input_female_features = ["a photo of a woman who is " + f for f in AnalyzeConfig.female_features]
    input_male_features = ["a photo of a man who is " + f for f in AnalyzeConfig.male_features]
    input_classes = input_female_features if usertype == 'female' else input_male_features
    input_features = AnalyzeConfig.female_features if usertype == 'female' else AnalyzeConfig.male_features 
  
    ## Evaluate Model
    result_dicts_array = []
    
    ## One Image
    imgdata = base64.b64decode(imgbase64)
    dataBytesIO = io.BytesIO(imgdata)
    image = Image.open(dataBytesIO)
    inputs = AnalyzeConfig.CLIP_processor(text=input_classes, images=image, return_tensors="pt", padding=True)
    outputs = AnalyzeConfig.CLIP_model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)  
    
    ## Sort and Print Factors
    unsorted_dict = dict(zip(input_features, torch.round(probs[0], decimals = 3).detach().numpy()))
    sorted_dict = sorted(unsorted_dict.items(), key = lambda item: item[1], reverse = True)
    
    return sorted_dict
    
    


def CLIP_result_base64s(imgbase64s, usertype):
    input_female_features = ["a photo of a woman who is " + f for f in AnalyzeConfig.female_features]
    input_male_features = ["a photo of a man who is " + f for f in AnalyzeConfig.male_features]
    input_classes = input_female_features if usertype == 'female' else input_male_features
    input_features = AnalyzeConfig.female_features if usertype == 'female' else AnalyzeConfig.male_features 

    ## Evaluate Model
    result_dicts_array = []
    
    for i in range(len(imgbase64s)):
        imgdata = base64.b64decode(imgbase64s[i])        
        dataBytesIO = io.BytesIO(imgdata)
        image = Image.open(dataBytesIO)
        inputs = AnalyzeConfig.CLIP_processor(text=input_classes, images=image, return_tensors="pt", padding=True)
        outputs = AnalyzeConfig.CLIP_model(**inputs)
        logits_per_image = outputs.logits_per_image # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
        
        # Save to `result_dicts_array`
        unsorted_dict = dict(zip(input_features, torch.round(probs[0], decimals = 3).detach().numpy()))
        result_dicts_array.append(unsorted_dict)
        
        # DEBUG
        print(f'{i}th image analysis finished')
      
    return_dict = {}
    for k in result_dicts_array[0].keys():
        return_dict[k] = sum(d[k] for d in result_dicts_array)
        
    sorted_dict = sorted(return_dict.items(), key = lambda item: item[1], reverse = True)
    
    return sorted_dict    
  

def get_account_CLIP_result(request):
        
    body_data = json.loads(request.body)
    profile_base64 = body_data.get('profile')
    feed_base64 = body_data.get('feeds')
    feed_base64.append(profile_base64)
    
    result_array = CLIP_result_base64s(feed_base64, body_data.get('type'))
    
    # Extracting Top 3
    feature1 = result_array[0][0]
    score1 = result_array[0][1]
    feature2 = result_array[1][0]
    score2 = result_array[1][1]
    feature3 = result_array[2][0]
    score3 = result_array[2][1]
    
    score_total = score1 + score2 + score3
    score1 = math.floor(score1 * 100 / score_total)
    score2 = math.floor(score2 * 100 / score_total)
    score3 = math.floor(score3 * 100 / score_total)
    
    return_json = {
        "feature1": feature1,
        "score1": score1,
        "feature2": feature2,
        "score2": score2,
        "feature3": feature3,
        "score3": score3
    }
    
    return HttpResponse(json.dumps(return_json), content_type = "application/json")


def get_img_CLIP_result(request):
    body_data = json.loads(request.body)
    img_base64 = body_data.get('img')
    
    result_array = CLIP_result_one_img(img_base64, body_data.get('type'))
    
    # Extracting Top 3
    feature1 = result_array[0][0]
    score1 = result_array[0][1]
    feature2 = result_array[1][0]
    score2 = result_array[1][1]
    feature3 = result_array[2][0]
    score3 = result_array[2][1]
    
    score_total = score1 + score2 + score3
    score1 = math.floor(score1 * 100 / score_total)
    score2 = math.floor(score2 * 100 / score_total)
    score3 = math.floor(score3 * 100 / score_total)
    
    return_json = {
        "feature1": feature1,
        "score1": score1,
        "feature2": feature2,
        "score2": score2,
        "feature3": feature3,
        "score3": score3
    }
    
    return HttpResponse(json.dumps(return_json), content_type = "application/json")
    
