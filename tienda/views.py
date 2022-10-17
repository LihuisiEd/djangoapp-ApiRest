
from django.shortcuts import render

from.models import Producto, Categoria

from rest_framework.views import APIView
from rest_framework.response import Response
 
from .serializers import ProductoSerializer
 
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class SeriesView(APIView):
    
    def get(self,request):
        dataSeries = Producto.objects.all()
        serSeries = ProductoSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = ProductoSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class SerieDetailView(APIView):
    
    def get(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        serSerie = ProductoSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        serSerie = ProductoSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        serSerie = ProductoSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)

    
