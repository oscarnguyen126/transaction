# Generated by Django 3.2.23 on 2024-02-06 09:28

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, help_text='Tên', max_length=250, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Thời điểm cập nhật')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('full_name', models.CharField(blank=True, help_text='Họ và tên', max_length=250, null=True)),
                ('birthday', models.DateField(blank=True, help_text='Ngày sinh', null=True)),
                ('phone', models.CharField(blank=True, help_text='Số điện thoại', max_length=20, null=True)),
                ('bank_acc', models.IntegerField(blank=True, help_text='Số tài khoản', max_length=250, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Thời điểm cập nhật')),
                ('bank', models.ForeignKey(editable=False, help_text='Ngân hàng', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_mng_user_bank', to='user_Mng.bank')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
