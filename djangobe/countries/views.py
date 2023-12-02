from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer



# Create your views here.
class CountryView(APIView):
  def get(self, request):
     countries = Country.objects.all()
     serializer = CountrySerializer(countries, many=True)
     print(serializer.data)
     return Response(serializer.data)

  def post(self, request):
      serializer = CountrySerializer(data=request.data)
      if serializer.is_valid():
          serializer.save() # This line saves the data to the database
          return Response(serializer.data, status=201)
      return Response(serializer.errors, status=400)