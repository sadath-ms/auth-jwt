# Generated by Django 3.1.1 on 2020-09-24 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(blank=True, max_length=30, null=True)),
                ('role_description', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['pk'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_id', to='jwt_auth.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
                'managed': True,
                'unique_together': {('role', 'user')},
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userpermissions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jwt_auth.userpermissions')),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=20, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(null=True)),
            ],
            options={
                'ordering': ['pk'],
                'managed': True,
            },
            bases=('jwt_auth.userpermissions',),
        ),
    ]
