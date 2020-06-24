import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Conductor(models.Model):

    user = models.OneToOneField("users.User", verbose_name=_(""),
                                on_delete=models.CASCADE)
    national_id_number = models.CharField(_("Conductor National Id Number"), max_length=50)
    phone = models.PhoneNumberField(_("Conductor's Phone Number"))
    attribute = models.ManyToManyField("conductors.Attribute",
                                       verbose_name=_("Attributes that Conductor has"))

    class Meta:
        verbose_name = _("Conductor")
        verbose_name_plural = _("Conductors")

    def __str__(self):
        return self.user.get_full_name

    def get_absolute_url(self):
        return reverse("conductor:detail", kwargs={"pk": self.pk})


class ConductorLike(models.Model):

    id = models.UUIDField(_("Conductor Like Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who liked Conductor"),
                             on_delete=models.CASCADE)
    psv = models.ForeignKey("conductors.Conductor", verbose_name=_("Conductor liked by user"),
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Psv Like")
        verbose_name_plural = _("Psv Likes")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("conductor_like:detail", kwargs={"pk": self.pk})


class ConductorFavourite(models.Model):

    id = models.UUIDField(_("Conductor Favourite Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who favourited Conductor"),
                             on_delete=models.CASCADE)
    Conductor = models.ForeignKey("conductors.Conductor",
                                  verbose_name=_("Conductor favourited by user"),
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Conductor Favourite")
        verbose_name_plural = _("Conductor Favourites")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("conductor_favourite:detail", kwargs={"pk": self.pk})


class Attribute(models.Model):

    name = models.CharField(_("Psv Attribute"), max_length=50)

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("attribute:detail", kwargs={"pk": self.pk})
