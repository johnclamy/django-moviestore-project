# Generated by Django 5.0 on 2024-12-31 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('descr', models.TextField()),
                ('image', models.ImageField(upload_to='movie_imgs/')),
            ],
        ),
    ]