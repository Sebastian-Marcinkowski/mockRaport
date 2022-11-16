from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import RaportSerializer
from django.http import JsonResponse

# Create your views here.
@api_view(['POST'])
def raportEndpoint(rrequest):
    """
    Function for posting mock raport
    """
    raport = JSONParser().parse(rrequest)
    raportSerialized = RaportSerializer(data=raport)

    if raportSerialized.is_valid():
        raport = raportSerialized.save()
        sendData = RaportSerializer(raport, many=False)
        return JsonResponse(sendData.data, safe=False)
    return JsonResponse(None, safe=False)