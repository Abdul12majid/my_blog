# Generated by Django 5.1 on 2024-11-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_remove_post_categories_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.IntegerField(default=0),
        ),
    ]