from django.shortcuts import render
from .models import *
from .serializers import CustomerSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


@api_view(['GET','POST'])
def customer(request,format=None):

    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializers(customer, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def create_customer(request, format=None):

    if request.method == 'POST':
        customer = CustomerSerializers(data=request.data)

        if Customer.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This customer already exist')

        if customer.is_valid():
            customer.save()
            return Response(customer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT'])
def update_customer(request,id,format=None):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializers(customer)
        return(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializers(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request,id,format=None):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        customer = Customer.objects.get(pk=id)
        customer.delete()
    return Response(status=status.HTTP_202_ACCEPTED)





