from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FocusLog, Tag
from .serializers import FocusLogSerializer, TagSerializer

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

class TagsIndex(APIView):
    def get(self, request):
        try:
            queryset = Tag.objects.all()
            serializer = TagSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
