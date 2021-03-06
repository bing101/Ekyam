# Generated by Django 2.0.2 on 2018-03-30 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enetwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_title', models.CharField(max_length=30)),
                ('problem_description', models.TextField(max_length=2500)),
                ('problem_category', models.CharField(choices=[('Technical/software', 'Entrepreneur'), ('ministry', 'Mentor'), ('hardware', 'Investor'), ('Job seeker', 'Job Seeker')], max_length=50)),
                ('problem_field', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='teambuild',
            name='user',
        ),
        migrations.DeleteModel(
            name='TeamBuild',
        ),
    ]
