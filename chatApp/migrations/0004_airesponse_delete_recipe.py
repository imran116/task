# Generated by Django 5.0.3 on 2024-03-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0003_rename_message_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('ai_response', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
