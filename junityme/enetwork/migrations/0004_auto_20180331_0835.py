# Generated by Django 2.0.2 on 2018-03-31 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enetwork', '0003_remove_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='problem_category',
            field=models.CharField(choices=[('Technical/software', 'Entrepreneur'), ('Government Ministry', 'Mentor'), ('Hardware', 'Investor'), ('Business', 'Business'), ('Management', 'management')], max_length=50),
        ),
    ]