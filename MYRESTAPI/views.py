from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import generics

global data;
data=['test']


class myRestView(APIView):

  def get(self,request,format=None):
       message={
           'Response':200,
           'Message':'Welcome to Django RestAPI',
           'data':data
       }
       return Response(message); 

   def post(self,request,format=None):
       new_Data=request.data
       name=new_Data.get('name',None)
       data.append(name)
       message={
           'Response':200,
           'Message':'Welcome to Django RestAPI',
           'data':data
       }
       return Response(message); 
      
# Creating API
from .serializer import mySerializer
class machstatzData(generics.CreateAPIView):
    serializer_class=mySerializer
    
    def create(self,request,*args,**kwargs):
        try:
            Length=request.data.get('Length')
            Quantity=request.data.get('Quantity')
            Weight=request.data.get('Weight')
            return super().create(request,*args,**kwargs)
        except Exception as e:
            return Response({
                "message":"Oops your data wrong....!"
            })
