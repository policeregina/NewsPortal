# Generated by Django 4.1.5 on 2023-02-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0009_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='can_create_post',
            field=models.CharField(default='True', max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
