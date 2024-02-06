from .models import User, Bank
from .serializers import UserSerializer, UserListSerializer, UserUpdateSerializer, BankSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return JsonResponse(UserListSerializer(users, many=True).data, safe=False, status=200)


    def post(self, request):
        user = User.objects.filter(username=request.data['username'])
        if len(user):
            return JsonResponse({"msg":"This username is already in use"}, status=400)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return JsonResponse(serializer.data, status=201, safe=False)


class UserDetails(APIView):
    def get_user(self, slug):
        return get_object_or_404(User, uuid=slug)

    def get(self, request, slug):
        user = self.get_user(slug)
        serializer = UserListSerializer(user)
        return JsonResponse(serializer.data)

    def put(self, request, slug):
        user = self.get_user(slug)
        serializer = UserUpdateSerializer(user, data=request.data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        
        serializer.save()
        return JsonResponse(serializer.data, status=200)

    def delete(self, request, slug):
        user = self.get_user(slug)
        user.delete()
        return JsonResponse({"msg": "User deleted successfully"}, status=204)


class BankList(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        return JsonResponse(UserListSerializer(banks, many=True).data, safe=False, status=200)


    def post(self, request):
        bank = Bank.objects.filter(name=request.data['name'])
        if len(bank):
            return JsonResponse({"msg":"This bank is already in use"}, status=400)

        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            bank = serializer.save()
            bank.save()
            return JsonResponse(serializer.data, status=201, safe=False)


class BankDetails(APIView):
    def get_bank(self, slug):
        return get_object_or_404(Bank, uuid=slug)

    def get(self, request, slug):
        bank = self.get_bank(slug)
        serializer = BankSerializer(bank)
        return JsonResponse(serializer.data)

    def put(self, request, slug):
        bank = self.get_bank(slug)
        serializer = BankSerializer(bank, data=request.data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        
        serializer.save()
        return JsonResponse(serializer.data, status=200)

    def delete(self, request, slug):
        bank = self.get_bank(slug)
        name = bank['name']
        bank.delete()
        return JsonResponse({"msg": '%s deleted successfully' % (name)}, status=204)
