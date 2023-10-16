# Generated by Django 4.2.3 on 2023-10-14 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('you_know', '0008_customuser_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sub',
            field=models.CharField(db_index=True, default='.', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='custom_user',
            field=models.ForeignKey(db_column='custom_user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='sub'),
        ),
    ]