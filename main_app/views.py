from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FocusLog, Tag, Distraction, ToDoList, Task
from .serializers import FocusLogSerializer, TagSerializer, DistractionSerializer, ToDoListSerializer, TaskSerializer

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Create your views here.
User = get_user_model()

class SignupUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.data.get("username")
            email = request.data.get("email")
            password = request.data.get("password")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            
            if not username or not password or not email or not first_name or not last_name:
                return Response(
                    {"error": "Please provide a username, password, and email"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(username=username).exists():
                return Response(
                    {'error': "User Already Exisits"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif first_name and last_name and username and password and email:
                user = User.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                return Response(
                    {"id": user.id, "username": user.username, "email": user.email},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Homepage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'DotDiary Homepage'}
        return Response(content)

class FocusLogsIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            queryset = FocusLog.objects.all()
            serializer = FocusLogSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = FocusLogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FocusLogSession(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, session_id):
        try:
            queryset = get_object_or_404(FocusLog, id=session_id)
            serializer = FocusLogSerializer(queryset)
            session_distractions = Distraction.objects.filter(focuslog=session_id)
            distractions_list = Distraction.objects.exclude(id__in = queryset.distraction.all().values_list('id'))
            
            data = serializer.data
            data['session_distractions'] = DistractionSerializer(session_distractions, many=True).data
            data['distractions_list'] = DistractionSerializer(distractions_list, many=True).data
            
            return Response(data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, session_id):
        try:
            queryset = get_object_or_404(FocusLog, id=session_id)
            serializer = FocusLogSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, session_id):
        try:
            queryset = get_object_or_404(FocusLog, id=session_id)
            queryset.delete()
            return Response({'message': f'Your Focus session with id #{session_id} has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagsIndex(APIView):
    def get(self, request):
        try:
            queryset = Tag.objects.all()
            serializer = TagSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AssignDistraction(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, session_id, distraction_id):
        try:
            session = get_object_or_404(FocusLog, id=session_id)
            distractions = get_object_or_404(Distraction, id=distraction_id)
            session.distraction.add(distractions)
            
            session_distractions = Distraction.objects.filter(focuslog=session_id)
            distractions_list = Distraction.objects.exclude(id__in = session.distraction.all().values_list('id'))
            return Response({
                "session_distractions": DistractionSerializer(session_distractions, many=True).data,
                "distractions_list": DistractionSerializer(distractions_list, many=True).data
                }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UnassignDistraction(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, session_id, distraction_id):
        try:
            session = get_object_or_404(FocusLog, id=session_id)
            distractions = get_object_or_404(Distraction, id=distraction_id)
            session.distraction.remove(distractions)
            
            session_distractions = Distraction.objects.filter(focuslog=session_id)
            distractions_list = Distraction.objects.exclude(id__in = session.distraction.all().values_list('id'))
            return Response({
                "session_distractions": DistractionSerializer(session_distractions, many=True).data,
                "distractions_list": DistractionSerializer(distractions_list, many=True).data
                }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ToDoListsIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            queryset = ToDoList.objects.all()
            serializer = ToDoListSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ToDoListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ToDoListDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todolist_id):
        try:
            queryset = get_object_or_404(ToDoList, id=todolist_id)
            serializer = ToDoListSerializer(queryset)
            tasks = Task.objects.filter(todolist=todolist_id)
            
            data = serializer.data
            data['tasks'] = TaskSerializer(tasks, many=True).data
            
            return Response(data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, todolist_id):
        try:
            queryset = get_object_or_404(ToDoList, id=todolist_id)
            serializer = ToDoListSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, todolist_id):
        try:
            queryset = get_object_or_404(ToDoList, id=todolist_id)
            queryset.delete()
            return Response({'message': f'Your todolist with id #{todolist_id} has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TasksIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todolist_id):
        try:
            queryset = Task.objects.filter(todolist=todolist_id)
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, todolist_id):
        serializer = TaskSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            queryset = Task.objects.filter(todolist=todolist_id)
            serializer= TaskSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskToDo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todolist_id, task_id):
        try:
            queryset = get_object_or_404(Task.objects.filter(todolist=todolist_id), id=task_id)
            serializer = TaskSerializer(queryset)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, todolist_id, task_id):
        try:
            queryset = get_object_or_404(Task.objects.filter(todolist=todolist_id), id=task_id)
            serializer = TaskSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, todolist_id, task_id):
        try:
            queryset = get_object_or_404(Task.objects.filter(todolist=todolist_id), id=task_id)
            queryset.delete()
            return Response({'message': f'Your task number #{task_id} has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)