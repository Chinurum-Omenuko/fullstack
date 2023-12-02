from django.shortcuts import render, HttpResponse
import httpx
from django.http import JsonResponse

# Create your views here.
async def get_users(request):
    url = "https://jsonplaceholder.typicode.com/users"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        user_info = response.json()
        return JsonResponse(user_info)