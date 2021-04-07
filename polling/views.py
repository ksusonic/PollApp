from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Poll as PollModel, PollQuestion as QuestionModel, User, Vote
from .serializers import PollSerializer, QuestionListSerializer, UserSerializer, VoteSerializer, UserVoteSerializer


class ActivePolls(viewsets.ReadOnlyModelViewSet):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer

    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all().filter(poll=pk)
        serializer = QuestionListSerializer(queryset, many=True)
        return Response(serializer.data)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        queryset = Vote.objects.all().filter(user_id=pk)
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)


class VoteView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = UserVoteSerializer

    def update(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, pk=None):
        queryset = QuestionModel.objects.all().filter(poll_id=pk)
        serializer = QuestionListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        vote = Vote.objects.get(question__vote=pk)
        serializer = UserVoteSerializer(data=request.data)
        if serializer.is_valid():
            vote.save()
        return Response({'status': 'answer saved'})
