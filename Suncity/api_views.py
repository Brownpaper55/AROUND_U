from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Program, CustomUser
from datetime import date
from .serializers import (
    ProgramSerializer, 
    ProgramListSerializer, 
    ProgramDetailSerializer,
    CustomUserSerializer,
    CustomUserCreateSerializer)

#user authentication
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register a new user"""
    serializer = CustomUserCreateSerializer(data = request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user = user)
        return Response(
            {
                'user':CustomUserSerializer(user).data,
                'token':token.key,
                'message': "user registered successfully"
            }, status = status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Login user and return token"""
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not  password:
        return Response({
            'error': 'Username or password required'
        }, status = status.HTTP_400_BAD_REQUEST)
    user = authenticate(username = username, password = password)
    if user:
        token, created = Token.objects.get_or_create(user = user)
        return Response({
            'user': CustomUserSerializer(user).data,
            'token':token.key,
            'message': 'Login successful'
        },status = status.HTTP_200_OK)
    return Response({
        'error': 'invalid user'
    }, status = status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    """Logout user by deleting token"""
    try:
        request.user.auth_token.delete()
        return Response({
            'message': 'Logout successful'
        }, status=status.HTTP_200_OK)
    except:
        return Response({
            'error': 'Error logging out'
        }, status=status.HTTP_400_BAD_REQUEST)
    

#user profile view
@api_view(['GET'])
@permission_classes([IsAuthenticated])

def profile(request):
    """view current user profile"""
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status= status.HTTP_200_OK)

#update current user profile
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    """Update current user profile"""
    serializer = CustomUserSerializer(
        request.user, 
        data=request.data, 
        partial=request.method == 'PATCH'
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Program views
@api_view(['GET'])
@permission_classes([AllowAny])
def program_list(request):
    programs = Program.objects.all().order_by('-Date')

    #optional filtering
    location =  request.query_params.get('location')
    date = request.query_params.get('Date')

    if location:
        programs = programs.filter(Location_icontains = location)
    if date:
        programs = programs.filter(Date_icontains = date)

    serializer = ProgramListSerializer(programs, many=True)
    return Response({
        'count':programs.count,
        'programs': serializer.data
    }, status = status.HTTP_200_OK)

#Get detailed view of a particular program
@api_view(['GET'])
@permission_classes([AllowAny])
def program_detail(request, pk):
    program = get_object_or_404(Program,pk=pk)

    #increment view count
    Program.objects.filter(pk=pk).update(views = F('views')+1)
    program.refresh_from_db

    serializer = ProgramDetailSerializer(program)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def program_create(request):
    """Create a new program"""
    serializer = ProgramSerializer(request.data, context = {'request':request})
    if serializer.is_valid():
        program = serializer.save(user = request.user)
        return Response(
            ProgramDetailSerializer(program).data,
            status = status.HTTP_200_CREATED
        )

@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def program_update(request, pk):
    """update  program"""
    program = get_object_or_404(Program, pk= pk)
    #check if user owns the program
    if program.user != request.user:
        return Response(
            {
                'error':'You can only update your own programs'
            }, status = status.HTTP_403_FORBIDDEN
        )
    serializer = ProgramSerializer(program, data = request.data,partial = request.method == 'PATCH', context = {'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data, status = status.HTTP_200_OK
        )
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def program_delete(request,pk):
    """Delete program by owner"""
    program = get_object_or_404(Program, pk=pk)
    #check if user owns the program
    if request.user != program.user:
        return Response({
            'error':'You can only delete your own programs'
        }, status = status.HTTP_403_FORBIDDEN)
    program.delete()
    return Response(
        {'message':'Program deleted successfully'}, status= status.HTTP_204_NO_CONTENT
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_programs(request):
    """Get all programs created by current user"""
    programs = Program.objects.filter(user = request.user).order_by('-Date')
    serializers = ProgramSerializer(programs, many=True)
    return Response({
        'count':programs.count,
        'programs': serializers.data
    }, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_programs(request, user_id):
    """Get all programs created by a specific user"""
    user = get_object_or_404(CustomUser, pk = user_id)
    programs = Program.objects.filter(user = user).order_by('-Date')
    serializers = ProgramSerializer(programs, many=True)
    return Response({
        'count':programs.count,
        'programs': serializers.data
    }, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def popular_programs(request):
    """Popular programs"""
    programs = Program.objects.all().order_by('-views')[:10]#Top 10 most viewed
    serializer = ProgramSerializer(programs, many=True)
    return Response({
        'Programs':serializer.data
    }, status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def upcoming_programs(request):
    programs = Program.objects.filter(Date__gte = date.today()).order_by('Date')
    serializer = ProgramSerializer(programs, many=True)
    return Response({
        'count':programs.count(),
        'program':serializer.data
    }, status =status.HTTP_200_OK)
