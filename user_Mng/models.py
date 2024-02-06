from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password

 
class Bank(models.Model):
    uuid = models.UUIDField(default=UUID4,
                                max_length=64,
                                editable=False,
                                unique=True,
                                primary_key=True,
                            )
    name = models.CharField(
                                editable=True,
                                blank=True,
                                null=True,
                                max_length=250,
                                help_text=_('Tên'),
                            )
    created_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm tạo'),
                            )
    updated_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm cập nhật'),
                            )
    
    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    uuid = models.UUIDField(default=UUID4,
                                max_length=64,
                                editable=False,
                                unique=True,
                                primary_key=True,
                            )
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=20)
    full_name = models.CharField(
                                editable=True,
                                blank=True,
                                null=True,
                                max_length=250,
                                help_text=_('Họ và tên'),
                            )
    birthday = models.DateField(
                                editable=True,
                                blank=True,
                                null=True,
                                help_text=_('Ngày sinh'),
                            )
    phone = models.CharField(
                                editable=True,
                                blank=True,
                                null=True,
                                max_length=20,
                                help_text=_('Số điện thoại'),
                            )
    bank = models.ForeignKey(Bank,
                                to_field='uuid',
                                related_name='%(app_label)s_%(class)s_bank',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Ngân hàng'),
                            )
    bank_acc = models.IntegerField(
                                editable=True,
                                blank=True,
                                null=True,
                                max_length=250,
                                help_text=_('Số tài khoản'),
                            )
    created_at = models.DateTimeField(
                                editable=False,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm tạo'),
                            )
    updated_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm cập nhật'),
                            )


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        self.password = make_password(self.password)
        super().save(self, *args, **kwargs)
