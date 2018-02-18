# Generated by Django 2.0 on 2017-12-15 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0004_auto_20171201_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='markers_marker_create_by', to=settings.AUTH_USER_MODEL),
        ),
    ]