# Generated by Django 4.0.1 on 2023-09-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_genre_book_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=123)),
                ('city', models.CharField(max_length=123)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hello.author')),
            ],
        ),
    ]