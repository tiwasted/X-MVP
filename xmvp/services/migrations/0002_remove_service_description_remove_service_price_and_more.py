# Generated by Django 4.2.1 on 2024-02-19 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='sub_service',
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='Default Service Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subservices', to='services.service')),
            ],
        ),
    ]
