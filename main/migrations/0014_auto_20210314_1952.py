# Generated by Django 3.1.7 on 2021-03-14 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210314_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tests_questions',
            options={'verbose_name': 'question in test', 'verbose_name_plural': 'questions in tests'},
        ),
        migrations.AddField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='roles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='roles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]