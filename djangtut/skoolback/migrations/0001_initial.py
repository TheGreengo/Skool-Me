# Generated by Django 4.2.7 on 2024-01-01 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlashDecks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skoolback.student')),
            ],
        ),
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=1000)),
                ('back', models.CharField(max_length=1000)),
                ('last', models.DateTimeField()),
                ('starred', models.BooleanField(default=False)),
                ('deck_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skoolback.flashdecks')),
            ],
        ),
    ]
