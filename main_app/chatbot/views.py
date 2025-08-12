import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

genai.configure(api_key="YOUR_API_KEY")  # 🔁 Replace with your API key
model = genai.GenerativeModel("gemini-pro")


@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get("message")

        response = model.generate_content(user_input)
        return JsonResponse({"reply": response.text})
    return JsonResponse({"error": "Invalid request"}, status=400)
