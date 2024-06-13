
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class TodoViewset(viewsets.ViewSet):
    queryset = Todo.objects.all()

    def list(self, request):
        ser_data = TodoSerializer(instance=Todo.objects.all(), many=True)
        return Response(data=ser_data.data)

    def create(self, request):
        ser_data = TodoSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.validated_data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        ser_data = TodoSerializer(instance=todo)
        return Response(data=ser_data.data)

    def partial_update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        ser_data = TodoSerializer(
            instance=todo, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.validated_data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
