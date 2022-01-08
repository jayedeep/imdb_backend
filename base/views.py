from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import MoviesSerializers
from . models import Movies
# Create your views here.
import django_filters
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class MoviesApi(APIView):
    search_fields = ('^name', '^description')
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk=None,sorted_by=None,format=None):
        if request.method=="GET":
            id=pk
            queryset = Movies.objects.all()
            sort_by = sorted_by
            print(">>>>>>>>>sort by\n\n\n\n\n\n\n\n",sort_by)

            if id is not None:
                movie=Movies.objects.get(id=id)
                serializer=MoviesSerializers(movie)
                return Response(serializer.data)
            else:
                movie=Movies.objects.all()
                if sort_by is not None:
                    if sort_by == 'rating':
                        movie = movie.order_by('-rating')
                    elif sort_by == 'realise_date':
                        movie = movie.order_by('-realise_date')
                    elif sort_by == 'duration':
                        movie = movie.order_by('-duration')
                    else:
                        movie = movie.order_by(sort_by)

                serializer=MoviesSerializers(movie,many=True)
                print(serializer.data)
                return Response(serializer.data,status=status.HTTP_200_OK)



    def post(self,request,format=None):
        serializer=MoviesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Saved"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        movie=Movies.objects.get(id=id)
        serializer=MoviesSerializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Record is Fully Updated"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        id=pk
        movie=Movies.objects.get(id=id)
        serializer=MoviesSerializers(movie,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Record is Partially Updated"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        id=pk
        movie=Movies.objects.get(id=id)
        movie.delete()
        return Response({"msg":"Record is Deleted"},status=status.HTTP_400_BAD_REQUEST)


class MoviesApiSearch(ListAPIView):
    permission_classes = (IsAuthenticated,)

    # queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['image_keyword']

    def get_queryset(self):
        queryset = Movies.objects.all()
        keywords = self.request.query_params.get('search')
        if keywords:
            print(">>>>\n\n\n\n\n",keywords)
            for ky in keywords.split(','):
                queryset = queryset.filter(Q(name__icontains=ky)|Q(description__icontains=ky))
        return queryset

    # search_fields = ['^name', '^description']