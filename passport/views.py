from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def api_root(request):
    """
    API root endpoint
    """
    return Response({
        'message': 'Passport Data Extraction API',
        'endpoints': {
            'extract': '/api/passport/extract/',
        }
    })

@api_view(['POST'])
def passport_extract(request):
    """
    Extract data from passport image
    """
    # This is a placeholder for the actual passport extraction logic
    return Response({
        'message': 'Passport extraction endpoint - ready for implementation',
        'status': 'success'
    }, status=status.HTTP_200_OK)
