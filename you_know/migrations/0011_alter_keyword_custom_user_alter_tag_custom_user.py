# Generated by Django 4.2.3 on 2023-10-23 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('you_know', '0010_alter_category_custom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='custom_user',
            field=models.ForeignKey(db_column='custom_user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sub'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='custom_user',
            field=models.ForeignKey(db_column='custom_user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sub'),
        ),
    ]
