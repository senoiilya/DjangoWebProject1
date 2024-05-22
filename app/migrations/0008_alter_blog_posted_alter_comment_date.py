# Generated by Django 4.2.11 on 2024-05-21 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 5, 21, 23, 33, 42, 612871), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 5, 21, 23, 33, 42, 612871), verbose_name='Дата комментария'),
        ),
    ]
