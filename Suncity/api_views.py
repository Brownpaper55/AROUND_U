from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Program
from .serializers import ProgramSerializer

@api_view(['GET'])
class AllPrograms(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

