# Generated by Django 5.2.1 on 2025-06-06 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_interpret_zanry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['nazev'], 'verbose_name': 'Album', 'verbose_name_plural': 'Alba'},
        ),
        migrations.AlterModelOptions(
            name='interpret',
            options={'ordering': ['jmeno'], 'verbose_name': 'Interpret', 'verbose_name_plural': 'Interpreti'},
        ),
        migrations.AlterModelOptions(
            name='zanr',
            options={'ordering': ['nazev'], 'verbose_name': 'Žánr', 'verbose_name_plural': 'Žánry'},
        ),
    ]
