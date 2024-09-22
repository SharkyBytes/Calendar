from rest_framework import viewsets, permissions, status
from .serializers import *
from rest_framework.response import Response
from .models import *

class AppointmentViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Appointments.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            appointment = self.queryset.get(pk=pk)
            serializer = self.serializer_class(appointment)
            return Response(serializer.data)
        except Appointments.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

 
    def destroy(self, request, pk=None):
        try:
            appointment = self.queryset.get(pk=pk)
            appointment.delete()
            return Response({"message": "Appointment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Appointments.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
