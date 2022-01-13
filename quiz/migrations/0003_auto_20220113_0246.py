# Generated by Django 3.1.7 on 2022-01-12 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_auto_20220112_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question', to='quiz.quizzes'),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.category'),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]