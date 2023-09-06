from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail

import uuid
import hashlib


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        db_index=True,
        editable=False
    )

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name=_("username"),
        max_length=150,
        unique=True,
        db_index=True,
        help_text="150文字以内で文字や数字を使うことができます（記号は「@/./+/-/_」のみ使用可能）。",
        validators=[username_validator],
        error_messages={
            "unique": "このユーザー名はすでに登録済みです。"
        }
    )
    first_name = models.CharField(verbose_name=_("first_name"), max_length=150, blank=True)
    last_name = models.CharField(verbose_name=_("last_name"), max_length=150, blank=True)
    email = models.EmailField(verbose_name=_("email"), unique=True, blank=False)

    is_superuser = models.BooleanField(
        verbose_name=_("is_superuser"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )

    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRE_FIELDS = ["email"]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class DeleteMailToken(models.Model):
    token = models.CharField(max_length=150, unique=True, db_index=True, blank=False)
    created_at = models.DateTimeField("created_at", default=timezone.now)

    @staticmethod
    def create(_, email: str):
        dt = timezone.now()
        sentence = email + dt.strftime('%Y%m%d%H%M%S')
        rand = hashlib.sha1(sentence.encode('utf-8')).hexdigest()
        DeleteMailToken.objects.create(token=rand)
        return rand

    class Meta:
        db_table = 'delete_mail_token'


class DeleteAccountReason(models.Model):
    question1 = models.BooleanField(verbose_name='使い方がわからない', default=False)
    question2 = models.BooleanField(verbose_name='同様のサービスを他で利用している', default=False, blank=True,)
    question3 = models.BooleanField(verbose_name='データ登録等操作がし辛い', default=False, blank=True,)
    message = models.TextField(verbose_name=_("message"), blank=True, null=True,)
    created_at = models.DateTimeField("created_at", default=timezone.now, db_index=True)

    class Meta:
        db_table = 'delete_account_reason'


class Library(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50, blank=False)
    content = models.TextField(verbose_name=_('content'), blank=True, null=True,)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'library'
        constraints = [
            models.UniqueConstraint(
                fields=["custom_user", "title"],
                name="library_unique"
            )
        ]


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50, blank=False)
    content = models.TextField(verbose_name=_('content'), blank=True, null=True,)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        constraints = [
            models.UniqueConstraint(
                fields=["custom_user", "library", "title"],
                name="category_unique"
            )
        ]


class Keyword(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50, blank=False)
    content = models.TextField(verbose_name=_('content'), blank=True, null=True,)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'keyword'
        constraints = [
            models.UniqueConstraint(
                fields=["custom_user", "library", "category", "title"],
                name="keyword_unique"
            )
        ]


class Tag(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50, blank=False)
    content = models.TextField(verbose_name=_('content'), blank=True, null=True, )
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'
        constraints = [
            models.UniqueConstraint(
                fields=["custom_user", "title"],
                name="tag_unique"
            )
        ]
