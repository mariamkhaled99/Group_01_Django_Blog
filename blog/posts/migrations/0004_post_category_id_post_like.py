# Generated by Django 4.1 on 2022-08-28 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_lib', to='categories.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(null=True),
        ),
    ]