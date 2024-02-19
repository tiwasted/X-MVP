# Generated by Django 4.2.1 on 2024-02-19 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_remove_service_description_remove_service_price_and_more'),
        ('orders', '0002_alter_order_sub_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service',
        ),
        migrations.AlterField(
            model_name='order',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='sub_service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='services.subservice'),
            preserve_default=False,
        ),
    ]
