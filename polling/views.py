from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Poll as PollModel, PollQuestion as QuestionModel
from .serializers import PollSerializer, QuestionListSerializer


class ActivePolls(viewsets.ReadOnlyModelViewSet):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer

    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all().filter(poll_id=pk)
        serializer = QuestionListSerializer(queryset, many=True)
        return Response(serializer.data)

