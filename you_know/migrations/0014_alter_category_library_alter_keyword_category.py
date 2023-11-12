# Generated by Django 4.2.3 on 2023-11-12 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('you_know', '0013_alter_keyword_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='you_know.library'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='you_know.category'),
        ),
    ]
