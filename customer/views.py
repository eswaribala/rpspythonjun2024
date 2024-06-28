from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view

from customer.models import Stock
from customer.serializers import StockSerializer


# Create your views here.

# CRUD operation -- Stock - create,retrieve,update or delete
@swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['id', 'name', 'type', 'price', 'qty', ' price_trending_date'],
        properties={
            'id': openapi.Schema(type=openapi.TYPE_NUMBER),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'type': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER),
            'qty': openapi.Schema(type=openapi.TYPE_NUMBER),
            'price_trending_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),
            # 'end_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),

        },
    ),
    operation_description='Create Stock',
    responses={200: ""}
)
@api_view(['GET', 'POST'])
def stock_list(request):
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            stock = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Stock created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


@swagger_auto_schema(
    methods=['put'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['id', 'name', 'type', 'price', 'qty', ' price_trending_date'],
        properties={
            'id': openapi.Schema(type=openapi.TYPE_NUMBER),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'type': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER),
            'qty': openapi.Schema(type=openapi.TYPE_NUMBER),
            'price_trending_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),
            # 'end_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),

        },
    ),
    operation_description='Update Customer',
    responses={200: ""}
)
@api_view(["GET", "PUT", "DELETE"])
def stock_parameterized_data(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(data={'The stock does not exist'}, status=400)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            stock_obj = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Stock updated successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(data={'Stock Deleted Successfully'}, status=200)


# web application
def add_stock(request):
    return render(request, 'add_stock.html')


def process_stock_entry(request):
    if request.method == 'POST':
        id = request.POST.get('stock_id')
        name= request.POST.get('stock_name')
        type = request.POST.get('stock_type')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        price_trending_date=request.POST.get('trending_date')
        # Create a new stock entry in the database using the Stock model
        stock = Stock(id=id,name=name,type=type,qty=qty,price=price,price_trending_date=price_trending_date)
        stock.save()

        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")
