# Generated by Django 4.2.2 on 2023-06-27 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0002_remove_student_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]