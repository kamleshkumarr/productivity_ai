from django.http import JsonResponse
from openai import OpenAI


def chat(request):
    msg = request.GET.get('msg')
    llm = OpenAI()
    response = llm(msg)
    return JsonResponse({'response': response})
