from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import Poll as PollModel, PollQuestion as PollQuestionModel
from .serializers import PollSerializer


class ActivePollsViewSet(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all().order_by('date_start')
