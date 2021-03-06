import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    id = models.UUIDField(_("Review Id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(_("First Name of User"), blank=True, max_length=255)
    last_name = models.CharField(_("Last Name of User"), blank=True, max_length=255)
    user_type = models.ManyToManyField("users.UserType", verbose_name=_("user types"),
                                       default="users.UserType.NORMAL_USER",)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name_slug(self):
        return slugify(f'{self.first_name} {self.last_name}')


class UserType(models.Model):

    DRIVER = 'driver'
    NORMAL_USER = 'normal_user'
    ADMIN = 'admin'
    USER_TYPE = [
        (DRIVER, _('User is a Driver')),
        (NORMAL_USER, _('User is a Normal User')),
        (ADMIN, _('User is an Admin')),
    ]

    name = models.CharField(
        max_length=32,
        choices=USER_TYPE,
    )

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users_types:detail", kwargs={"pk": self.pk})
