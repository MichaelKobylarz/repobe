# Generated by Django 5.1 on 2024-08-20 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0011_rename_name_movie_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_app.band')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm_app.person')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(through='orm_app.Membership', to='orm_app.person'),
        ),
    ]
