# Generated by Django 4.2.3 on 2023-11-03 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('you_know', '0012_remove_tag_keyword_keyword_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='tags',
            field=models.ManyToManyField(blank=True, to='you_know.tag'),
        ),
    ]
