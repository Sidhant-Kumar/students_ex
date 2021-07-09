from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import students
from .serializers import studentsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        stud = students.objects.all()

        name = request.query_params.get('first', None)
        if name is not None:
            stud = stud.filter(first__icontains=name)

        stud_serializer = studentsSerializer(stud, many=True)
        return JsonResponse(stud_serializer.data, safe=False)

    elif request.method == 'POST':
        stud_data = JSONParser().parse(request)
        stud_serializer = studentsSerializer(data=stud_data)
        if stud_serializer.is_valid():
            stud_serializer.save()
            return JsonResponse(stud_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(stud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = students.objects.all()
        return JsonResponse({'message': 'data deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    try:
        stud = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        stud_serializer = studentsSerializer(stud)
        return JsonResponse(stud_serializer.data)

    elif request.method == 'PUT':
        stud_data = JSONParser().parse(request)
        stud_serializer = studentsSerializer(stud, data=stud_data)
        if stud_serializer.is_valid():
            stud_serializer.save()
            return JsonResponse(stud_serializer.data)
        return JsonResponse(stud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stud.delete()
        return JsonResponse({'message': 'this student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def student_list_published(request):
    stud = students.objects.filter(published=True)

    if request.method == 'GET':
        stud_serializer = studentsSerializer(stud, many=True)
        return JsonResponse(stud_serializer.data, safe=False)
