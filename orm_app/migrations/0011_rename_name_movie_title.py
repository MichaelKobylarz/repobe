# Generated by Django 5.0.6 on 2024-07-10 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0010_actor_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
    ]
