# Generated by Django 4.2.3 on 2023-10-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('you_know', '0007_rename_uuid_customuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sub',
            field=models.CharField(db_index=True, default='.', max_length=150),
        ),
    ]
