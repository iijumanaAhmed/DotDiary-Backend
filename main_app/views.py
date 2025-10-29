from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FocusLog, Tag, Distraction, ToDoList
from .serializers import FocusLogSerializer, TagSerializer, DistractionSerializer, ToDoListSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class Homepage(APIView):
    def get(self, request):
        content = {'message': 'DotDiary Homepage'}
        return Response(content)

class FocusLogsIndex(APIView):
    def get(self, request):
        queryset = FocusLog.objects.all()
        serializer = FocusLogSerializer(queryset, many=True)
        return Response(serializer.data)

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