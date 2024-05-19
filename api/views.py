from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from django.contrib.auth import get_user_model

from app_main.models import Note
from .serializers import NoteSerializer, UserSerializer

User = get_user_model()

@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serialized_data = NoteSerializer(instance=notes, many=True)
    return Response(data=serialized_data.data)

@api_view(['POST'])
def create_note(request):
    if request.method == 'POST':
        owner_id = request.data['owner']
        title = request.data['title']
        body = request.data['body']

        user = User.objects.get(id=owner_id)
        note = Note.objects.create(owner=user, title=title, body=body)
        note.save()
        return Response(data='Created', status=status.HTTP_201_CREATED)

    return Response()

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialized_data = UserSerializer(instance=users, many=True)
    return Response(data=serialized_data.data)

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                password=serializer.validated_data['password']
            )
            user.save()
            return Response(data='Created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)