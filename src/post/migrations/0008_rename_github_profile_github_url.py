# Generated by Django 5.1 on 2024-08-19 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_profile_github_profile_linkedin_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='github',
            new_name='github_url',
        ),
    ]
