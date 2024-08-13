# views.py
from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer
# views.py

from .serializers import UserRegistrationSerializer
# views.py
from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer




