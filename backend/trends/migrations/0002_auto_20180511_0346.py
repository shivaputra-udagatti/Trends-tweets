# Generated by Django 2.0.5 on 2018-05-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetsTabl',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('name', models.TextField()),
                ('created', models.TextField()),
            ],
            options={
                'db_table': 'tweets_table',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='TweetsTable',
        ),
    ]
