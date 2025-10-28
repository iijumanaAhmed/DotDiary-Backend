from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FocusLog
from .serializers import FocusLogSerializer

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
