from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view(['GET', 'POST'])
def MenuItemsView (request):
    if request.method == 'GET':
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def SingleMenuItemView (request, pk):
    try:
        menu_item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        new_data = request.data
        serializer = MenuSerializer(menu_item, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu_item.delete()
        return Response({'message': 'Menu item was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def BookingViewSet(request):
    if request.method == 'GET':
        # List all bookings
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new booking
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def booking_detail(request, pk):
    try:
        # Retrieve the booking by primary key
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single booking
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update a booking
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a booking
        booking.delete()
        return Response({'message': 'Booking deleted successfully'}, status=status.HTTP_204_NO_CONTENT)