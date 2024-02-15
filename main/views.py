from django.shortcuts import render, redirect
import json

# Create your views here.

def change_lang(request):
    lang = request.GET.get("lang")
    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("preferred_language", lang)
    return response  
 
def home(request):
   
   preferred_language = request.COOKIES.get('preferred_language')
   language_code = preferred_language or "en"
  
   with open('static/langauges.json', 'r', encoding='utf-8') as f:
      context = json.load(f)
      context = context[language_code]


   context["lang"] = language_code
   if language_code == 'ar':
        context["dir"] = "rtl"
   return render(request,'main/index.html',context)  


def test(request):
   
   preferred_language = request.COOKIES.get('preferred_language')
   language_code = preferred_language or "en"
  
   with open('static/langauges.json', 'r', encoding='utf-8') as f:
      context = json.load(f)
      context = context[language_code]


   context["lang"] = language_code
   if language_code == 'ar':
        context["dir"] = "rtl"
   return render(request,'main/test.html',context)     

