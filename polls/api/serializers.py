from rest_framework import serializers

from polls.models import Question, Choice, Comment


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'choice_text',
            'votes',
            'question'
        )


class ChoiceSerializerForQuestion(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'choice_text',
            'votes'
        )


class CommentSerializerForQuestion(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'poster_name',
            'pub_date',
            'comment_text',
        )


class QuestionSerializer(serializers.ModelSerializer):
    #choices = serializers.PrimaryKeyRelatedField(many=True, queryset=Choice.objects.all())
    choices = ChoiceSerializerForQuestion(many=True)
    comments = CommentSerializerForQuestion(many=True)

    class Meta:
        model = Question
        fields = (
            'question_text',
            'pub_date',
            'choices',
            'comments'
        )
