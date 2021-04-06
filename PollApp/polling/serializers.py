from rest_framework.serializers import ModelSerializer
from .models import Poll, PollQuestion, Answer


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'name', 'date_start', 'date_end', 'description'
        ]


# class QuestionsInPollSerializer(ModelSerializer):
#     class Meta:
#         model = Q


class PollQuestionSerializer(ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = [
            'poll', 'question', 'question_type'
        ]
