from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView

from .models import Poll as PollModel, PollQuestion as PollQuestionModel
from .serializers import PollSerializer


class ActivePollsViewSet(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all().order_by('date_start')


class PollDetail(APIView):
    def get_object(self, pk):
        try:
            return PollModel.objects.get(pk=pk)
        except PollModel.DoesNotExist:
            raise Http404
