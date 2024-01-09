from rest_framework import generics
from .models import Program
from .serializers import ProgramSerializer

@api_view()
class AllPrograms(generics.ListAPIview):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

