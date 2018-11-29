# Generated by Django 2.0.5 on 2018-05-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0024_delete_tweetstable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetsTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('name', models.TextField()),
                ('created', models.TextField()),
                ('q', models.TextField()),
            ],
            options={
                'db_table': 'tweets_table',
                'managed': True,
            },
        ),
    ]