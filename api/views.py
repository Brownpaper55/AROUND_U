from rest_framework.response import Response
from rest_framework.decorators import api_view
from Suncity.models import Program
from .serializers import ProgramSerializer

@api_view(['GET'])
def get_data(request):
   program = Program.objects.all()
   serializer = ProgramSerializer(program, many=True)
   return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
   serializer = ProgramSerializer(data = request.data)
   if serializer.is_valid():
      return Response(serializer.data)
