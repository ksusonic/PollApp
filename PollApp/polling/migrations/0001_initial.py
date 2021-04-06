# Generated by Django 2.1.10 on 2021-04-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Новый опрос', max_length=255, verbose_name='Название опроса')),
                ('date_start', models.DateTimeField(auto_now=True, verbose_name='Дата старта')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('active', models.BooleanField(verbose_name='Опрос активен')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]