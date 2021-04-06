from rest_framework.serializers import ModelSerializer
from .models import Poll, PollQuestion


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'name', 'date_start', 'date_end', 'description'
        ]


class PollQuestionSerializer(ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = [
            'poll', 'question', 'question_type'
        ]
