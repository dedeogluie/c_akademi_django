from django.shortcuts import render
from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .permissions import IsStaffOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from django.db.models import Q

from datetime import date, datetime

# Create your views here.

class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer
    
    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queyset = Flight.objects.filter(date_of_departure__gt = today)

            if Flight.objects.filter(date_of_departure = today):
                today_queyset = Flight.objects.filter(estimated_time_of_departure__gt = current_time)

                queyset = queyset.union(today_queyset)
            return queyset

            # return Flight.objects.filter(Q(date_of_departure__gt=today) | Q(date_of_departure=today, estimated_time_of_departure__gt = current_time))

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    
    def get_queryset(self):
        queryset = super().get_queryset()  # == queryset = Reservation.objects.all()

        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user = self.request.user)
