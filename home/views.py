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

     start = time.time()
     df = pd.read_excel(file)

     translator = google_translator()

     for colname in df.columns:
          if colname in cols:
               df[colname] = df[colname].dropna().apply(translator.translate,lang_tgt='en')

     df.to_excel('ans.xlsx')

     end = time.time()
     print('time required : ', end - start)
     df.head(10)
     return True

# def translate(file, cols):
#      import pandas as pd
#      from google_trans_new import google_translator
#      import time
#      from googletrans import Translator, constants

#      start = time.time()
#      df = pd.read_excel(file)
#      print(len(list((df.columns))))

#      translator = google_translator()

#      for colname in df.columns:
#           if colname in cols:
#                df[colname] = df[colname].dropna().apply(translator.translate,lang_tgt='en')

#      df.to_excel('ans.xlsx')

#      end = time.time()
#      print('time required : ', end - start)
#      df.head(10)
#      return True