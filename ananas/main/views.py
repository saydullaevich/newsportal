import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

class ServerTimeView(APIView):
    def get(self, request):
        return Response({
            "time": datetime.datetime.now()
        })

