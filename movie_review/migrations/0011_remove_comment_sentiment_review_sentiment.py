# Generated by Django 5.1.5 on 2025-04-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0010_alter_comment_sentiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='sentiment',
        ),
        migrations.AddField(
            model_name='review',
            name='sentiment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
