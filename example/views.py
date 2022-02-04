from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics
from .serializers import LoginSerializer, ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
import pdb

# Create your views here.

class LoginApiView(APIView):

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response({"message":"please enter username and password"})
        try:
            account = User.objects.get(username=username)   
        except:
            return Response({'message':'user not exists'}, status=status.HTTP_400_BAD_REQUEST)
        token = Token.objects.get_or_create(user=account)[0].key
        if not check_password(password, account.password):
            return Response({"message": "Incorrect Login credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = account.username   
        login(request, account)
        return Response({'message':'User logged successfully','Token':token,'user':user}, status=status.HTTP_200_OK)


class AddProductApiView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Product.objects.all()

    def create(self, request):
        try:
            if request.data['secondary_memory'] == 'SSD' and request.data['secondary_storage'] == '1 TB' or request.data['secondary_storage'] == '2 TB':
                return Response({"message": "Combination of secondary memory=SSD and secondary storage>512 GB is not possible"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif request.data['cpu_company'] == 'AMD' and request.data['ram'] == '64' or request.data['ram'] == '128':
                return Response({"message": "Combination of cpu_compnay=AMD and ram >32 is not possible"},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Enter all required fields, cpu_company, ram, secondary_memory, secondary_storage, external_cooling"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Something went wrong"},
                                status=status.HTTP_400_BAD_REQUEST)

class EditProductApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Product.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            if request.data['secondary_memory'] == 'SSD' and request.data['secondary_storage'] == '1 TB' or request.data['secondary_storage'] == '2 TB':
                return Response({"message": "Combination of secondary memory=SSD and secondary storage>512 GB is not possible"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif request.data['cpu_company'] == 'AMD' and request.data['ram'] == '64' or request.data['ram'] == '128':
                return Response({"message": "Combination of cpu_compnay=AMD and ram >32 is not possible"},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Enter all required fields; cpu_company, ram, secondary_memory, secondary_storage, external_cooling"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            pk = self.kwargs.get('pk')
            instance = get_object_or_404(Product.objects.all(), pk=pk)
            serializer = ProductSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = get_object_or_404(Product.objects.all(), pk=pk)
        self.perform_destroy(instance)
        return Response({"message":"product deleted successfully"},status=status.HTTP_204_NO_CONTENT)



class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ram','secondary_memory']     




