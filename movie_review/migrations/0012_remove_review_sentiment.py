# Generated by Django 5.1.5 on 2025-04-03 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0011_remove_comment_sentiment_review_sentiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sentiment',
        ),
    ]
