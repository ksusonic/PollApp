from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Poll, PollQuestion, Vote, User


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'date_start', 'date_end')


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = ('question', 'answer_text', 'user_id')


class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = ('id', 'question', 'question_type')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserVoteSerializer(ModelSerializer):
    question = PrimaryKeyRelatedField(many=True, read_only=True)
    user_id = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Vote
        fields = ['question', 'user_id', 'answer_text']
