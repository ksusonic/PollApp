from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Poll, PollQuestion, Vote


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'date_start', 'date_end')


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = ('poll', 'answer_text', 'user_id')


class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = ('question', 'question_type')
