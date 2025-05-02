from rest_framework import generics
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from .permissions import IsActiveEmployee
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class NetworkNodeListCreateView(generics.ListCreateAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]  # Применяем права доступа
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['contacts__country']  # Фильтрация по стране
    search_fields = ['name']  # Поиск по имени


class NetworkNodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]