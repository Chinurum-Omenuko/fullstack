from rest_framework import generics
import httpx
from django.http import JsonResponse
from json.decoder import JSONDecodeError

async def get_event(request):
   url = "https://eonet.gsfc.nasa.gov/api/v2.1/events"
   async with httpx.AsyncClient() as client:
       response = await client.get(url)
       try:
           events = response.json()
       except JSONDecodeError:
           return JsonResponse({"error": "Invalid JSON response from server"}, status=400)
       return JsonResponse(events)
