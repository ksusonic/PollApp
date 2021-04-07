from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Poll as PollModel, PollQuestion as QuestionModel
from .serializers import PollSerializer, QuestionListSerializer


class ActivePollsViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all().order_by('date_start')


class QuestionViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all()
        questions = get_object_or_404(queryset, pk=pk)
        serializer = QuestionListSerializer
