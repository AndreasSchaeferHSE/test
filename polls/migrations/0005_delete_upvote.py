# Generated by Django 2.0.7 on 2018-07-17 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_upvote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
