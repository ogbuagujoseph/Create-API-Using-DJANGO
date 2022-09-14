from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.response import Response



# Create your views here.
@api_view(['POST'])
def createapi(request):
    record=CustomerSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def allapi(request):
    record=Customer.objects.all()
    record=CustomerSerializer(record, many=True)
    return Response(record.data)

@api_view(['DELETE'])
def deleteapi(request, id):
    record = Customer.objects.get(id=id)
    record.delete()
    return Response('API deleted Successfully')


@api_view(['GET'])
def detailapi(request, id):
    record = Customer.objects.get(id=id)
    info = CustomerSerializer(record, many=False)
    return Response(info.data)

@api_view(['PUT'])
def editapi(request, id):
    record = Customer.objects.get(id=id)
    info=CustomerSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('Update was successful')
    