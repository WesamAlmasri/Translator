from django.shortcuts import render, HttpResponse
from django.urls import path
from django.http import FileResponse


# Create your views here.
def Translator2(request):
     if request.method == 'POST' and request.FILES.get('file', None):
          file = request.FILES['file']
          cols = request.POST.getlist('columns')
          result = translate(file, cols)
          if result:
               return FileResponse(open('ans.xlsx', 'rb') )
     
     return render(request, 'Translator2.html')

def About(request):
     return render(request, 'About.html')
        
def translate(file, cols):
     import pandas as pd
     from google_trans_new import google_translator
     import time
     from googletrans import Translator, constants
     from pprint import pprint
     import io

     start = time.time()
     df = pd.DataFrame(pd.read_excel(file))
     print(len(list((df.columns))))

     dic = {}
     coldict = {}
     col =[]

     for colname in df.columns:
          col.append(colname)

     translator = google_translator()

     for colname in col:
          if colname in cols:
               translation = translator.translate(colname, lang_tgt="en")
               # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
               df[colname] = df[colname].dropna().apply(translator.translate,lang_tgt='en')

     df.to_excel('ans.xlsx')

     end = time.time()
     df.head(10)
     return True