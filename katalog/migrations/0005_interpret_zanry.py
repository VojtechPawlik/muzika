# Generated by Django 5.2.1 on 2025-06-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_album_obrazek_interpret_obrazek'),
    ]

    operations = [
        migrations.AddField(
            model_name='interpret',
            name='zanry',
            field=models.ManyToManyField(blank=True, to='katalog.zanr'),
        ),
    ]
