# Generated by Django 3.1.7 on 2022-01-11 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizzes',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='technique',
            field=models.IntegerField(choices=[(0, 'Multiple Choice'), (1, 'Single Choice')], default=0, verbose_name='Type of Question'),
        ),
    ]
