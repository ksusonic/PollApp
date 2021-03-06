from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Poll(models.Model):
    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    name = models.CharField(max_length=255, default="Новый опрос", verbose_name="Название опроса")
    date_start = models.DateTimeField(verbose_name="Дата старта", default=timezone.now)
    date_end = models.DateTimeField(verbose_name="Дата окончания", default=timezone.now() + timezone.timedelta(days=1))
    description = models.TextField(verbose_name="Описание")

    @property
    def active(self):
        if timezone.now() < self.date_end:
            return "Активен"
        else:
            return "Не активен"

    def __str__(self):
        return self.name


class PollQuestion(models.Model):
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    TEXT = 'T'
    ONE_ANSWER = 'O'
    MANY_ANSWERS = 'M'

    QUESTION_TYPES = [
        (TEXT, 'Текстовый ответ'),
        (ONE_ANSWER, 'Вопрос с одним ответом'),
        (MANY_ANSWERS, 'Вопрос с несколькими ответами')
    ]
    poll = models.ForeignKey(Poll, verbose_name="Опрос", on_delete=models.CASCADE)
    question = models.CharField(max_length=255, default="Новый вопрос", verbose_name="Вопрос")
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES, default=TEXT)

    @property
    def vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.question


class User(models.Model):
    class Meta:
        verbose_name = "Пользователь системы"
        verbose_name_plural = "Пользователи системы"
        ordering = ['id']
    name = models.CharField(max_length=255, default="Петя Иванов", verbose_name="Имя пользователя")

    def __str__(self):
        return self.name


class Vote(models.Model):
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['id']

        unique_together = ('question', 'user_id')

    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, default="ответ", verbose_name="Текст ответа")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
