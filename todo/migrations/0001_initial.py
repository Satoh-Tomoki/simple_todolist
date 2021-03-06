# Generated by Django 2.2.3 on 2020-09-02 06:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('deadline', models.DateTimeField(verbose_name='期限')),
                ('content', models.CharField(max_length=100, verbose_name='やること')),
            ],
            options={
                'db_table': 'todolist',
            },
        ),
    ]
