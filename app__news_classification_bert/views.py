from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from tensorflow.keras.models import load_model
from transformers import BertTokenizer, BertTokenizerFast
from transformers import TFAlbertModel, TFBertModel
import numpy as np
import os


os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model_name='app__news_classification_bert/best-model-albert-base-tf23/best-albert-base-chinese.h5'
model = load_model(model_name, custom_objects={"TFAlbertModel": TFAlbertModel})


tokenizer = BertTokenizerFast.from_pretrained('bert-base-chinese')


news_categories=['tw_stock_news', 'tw_macro', 'tw_quo', 'wd_macro', 'us_stock', 'eu_asia_stock', 'cn_macro', 'hk_stock', 'sh_stock']
idx2cate = { i : item for i, item in enumerate(news_categories)}


def home(request):
    return render(request, "app__news_classification_bert/home.html")


@csrf_exempt
def api_get_news_category(request):
    
    new_text = request.POST.get('input_text')

    category_prob = get_category_proba(new_text)

    return JsonResponse(category_prob)

def preprocessing_for_bert(input_sentences):
    result = tokenizer(
        text=list(input_sentences),
        add_special_tokens=True,
        max_length=250,
        truncation=True,
        #padding=True, 
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids = False,
        return_attention_mask = True,
        verbose = True)

    return result

def get_category_proba( text ):
    X_data = preprocessing_for_bert([text])
    X_newText = {'input_ids': X_data['input_ids'], 'attention_mask': X_data['attention_mask']}
    result = model.predict(X_newText)
    result_label = np.argmax(result, axis=-1)
    label = idx2cate[ result_label[0] ]
    proba = round(float(max(result[0])),2)
    proba = f'{proba*100:.0f}'
    return {'label': label, 'proba': proba}