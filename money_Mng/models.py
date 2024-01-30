from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from django.utils.translation import gettext as _
from user_Mng.models import User


class Transaction_Type(models.Model):
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
    created_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_created_by',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Người tạo'),
                            )
    created_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm tạo'),
                            )
    updated_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_updated_by',
                                on_delete=(models.PROTECT),
                                editable=True,
                                blank=False,
                                null=True,
                                help_text=_('Người cập nhật'),
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



class Transaction(models.Model):
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
    desc = models.TextField(
                                editable=True,
                                blank=True,
                                null=True,
                                max_length=2000,
                                help_text=_('Mô tả'),
                            )
    borrower = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_borrower',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Người vay'),
                            )
    lender =  models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_lender',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Người cho vay'),
                            )
    type = models.ForeignKey(Transaction_Type,
                                to_field='name',
                                related_name='%(app_label)s_%(class)s_type',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                            )
    amount = models.DecimalField(
                                editable=True,
                                blank=True,
                                null=True,
                                help_text=_('Số tiền'),
                                max_digits=19,
                                decimal_places=2,
                            )
    is_paid = models.BooleanField(
                                editable=True,
                                blank=True,
                                null=True,

                                default=True,

                                help_text=_('Đã thanh toán'),
                            )
    is_confirm = models.BooleanField(
                                editable=True,
                                blank=True,
                                null=True,

                                default=True,

                                help_text=_('Được xác nhận'),
                            )
    created_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_created_by',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Người tạo'),
                            )
    created_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm tạo'),
                            )
    updated_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_updated_by',
                                on_delete=(models.PROTECT),
                                editable=True,
                                blank=False,
                                null=True,
                                help_text=_('Người cập nhật'),
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
    created_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_created_by',
                                on_delete=(models.PROTECT),
                                editable=False,
                                blank=False,
                                null=True,
                                help_text=_('Người tạo'),
                            )
    created_at = models.DateTimeField(
                                editable=True,
                                blank=False,
                                null=False,
                                default=djnow,
                                help_text=_('Thời điểm tạo'),
                            )
    updated_by = models.ForeignKey(User,
                                to_field='username',
                                related_name='%(app_label)s_%(class)s_updated_by',
                                on_delete=(models.PROTECT),
                                editable=True,
                                blank=False,
                                null=True,
                                help_text=_('Người cập nhật'),
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