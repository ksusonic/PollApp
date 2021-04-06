# Generated by Django 2.1.10 on 2021-04-06 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0005_auto_20210406_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pollquestion',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 17, 12, 32, 289984, tzinfo=utc), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='pollquestion',
            name='question_type',
            field=models.CharField(choices=[('T', 'Текстовый ответ'), ('O', 'Вопрос с одним ответом'), ('M', 'Вопрос с несколькими ответами')], default='T', max_length=1),
        ),
    ]