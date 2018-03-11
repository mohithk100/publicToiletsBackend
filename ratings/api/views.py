from ratings.models import UserRatings,TotalRatings
from .serializers import UserRatingsCreationSerializer,TotalRatingsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CreateApiView(generics.CreateAPIView):
    queryset = UserRatings.objects.all()
    serializer_class = UserRatingsCreationSerializer
    permission_classes = (IsAuthenticated,)

class ViewUserRatings(generics.ListAPIView):
    serializer_class = UserRatingsCreationSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        username = self.kwargs['username']
        queryset = UserRatings.objects.filter(username=str(username))
        return queryset

class  OverallRatings(generics.ListAPIView):
    queryset = TotalRatings.objects.all()
    serializer_class = TotalRatingsSerializer
    permission_classes = (IsAuthenticated,)
