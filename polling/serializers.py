from rest_framework.serializers import ModelSerializer
from .models import Poll, PollQuestion, Vote


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'name', 'date_start', 'date_end', 'description'
        ]


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'answer_text')


class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = [
            'id', 'question', 'question_type'
        ]

