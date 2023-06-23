# Generated by Django 4.2.2 on 2023-06-22 15:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_remove_category_category_remove_post_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='카테고리'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blogapp.category'),
        ),
    ]
