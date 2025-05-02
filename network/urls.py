from django.urls import path
from .views import NetworkNodeListCreateView, NetworkNodeRetrieveUpdateDestroyView

urlpatterns = [
    path('network-nodes/', NetworkNodeListCreateView.as_view(), name='networknode-list-create'),
    path('network-nodes/<int:pk>/', NetworkNodeRetrieveUpdateDestroyView.as_view(), name='networknode-detail'),
]