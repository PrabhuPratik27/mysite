# Generated by Django 2.1.4 on 2018-12-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
