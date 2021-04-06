from rest_framework import generics
from .models import Poll as PollModel, PollQuestion as PollQuestionModel
from .serializers import PollSerializer


class Polls(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all()

