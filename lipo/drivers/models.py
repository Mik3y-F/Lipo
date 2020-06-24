from django.db import models
from django.utils.translation import ugettext_lazy as _


def get_image_filename(instance, filename):
    user_id = instance.user.id
    return f"driver/{user_id}/psv_license/"


class Driver(models.Model):

    user = models.OneToOneField("users.User", verbose_name=_(""),
                                on_delete=models.CASCADE)
    national_id_number = models.CharField(_("Driver National Id Number"), max_length=50)
    psvDrivingLicensePhoto = models.FileField(_("Photo of Driver's Psv driving license"),
                                              upload_to=get_image_filename, max_length=100)
    phone = models.PhoneNumberField(_("Driver's Phone Number"))
    attribute = models.ManyToManyField("drivers.Attribute",
                                       verbose_name=_("Attributes that driver has"))

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")

    def __str__(self):
        return self.user.get_full_name

    def get_absolute_url(self):
        return reverse("driver:detail", kwargs={"pk": self.pk})


class DriverLike(models.Model):

    id = models.UUIDField(_("Driver Like Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who liked Driver"),
                             on_delete=models.CASCADE)
    psv = models.ForeignKey("drivers.Driver", verbose_name=_("Driver liked by user"),
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Psv Like")
        verbose_name_plural = _("Psv Likes")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("driver_like:detail", kwargs={"pk": self.pk})


class DriverFavourite(models.Model):

    id = models.UUIDField(_("Driver Favourite Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who favourited Driver"),
                             on_delete=models.CASCADE)
    driver = models.ForeignKey("drivers.Driver", verbose_name=_("Driver favourited by user"),
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Driver Favourite")
        verbose_name_plural = _("Driver Favourites")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("driver_favourite:detail", kwargs={"pk": self.pk})


class Attribute(models.Model):

    name = models.CharField(_("Psv Attribute"), max_length=50)

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("attribute:detail", kwargs={"pk": self.pk})
