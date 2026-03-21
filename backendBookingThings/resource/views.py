from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Resource
from .serializers import ResourceSerializer


from .models import Reservation
from .serializers import ReservationSerializer
from .services import is_resource_available


# ERROR HANDLING
from rest_framework.exceptions import ValidationError

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]



class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        resource = serializer.validated_data['resource']
        date = serializer.validated_data['date']
        startAt = serializer.validated_data['startAt'].hour
        endsAt = serializer.validated_data['endsAt'].hour

        available, message = is_resource_available(resource, date, startAt, endsAt)

        if not available:
            raise ValidationError({"detail": message})

        serializer.save(user=self.request.user)