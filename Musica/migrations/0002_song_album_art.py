# Generated by Django 3.0.7 on 2020-07-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='Album_Art',
            field=models.CharField(blank=True, default='', max_length=1000000),
        ),
    ]
