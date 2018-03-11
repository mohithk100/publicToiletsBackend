from reviews.models import UserReviews
from .serializers import UserReviewSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CreateApiView(generics.CreateAPIView):
    queryset = UserReviews.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = (IsAuthenticated,)

class ViewReviews(generics.ListAPIView):
    serializer_class = UserReviewSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        place_id = self.kwargs['place_id']
        queryset = UserReviews.objects.filter(place_id=str(place_id))
        return queryset
