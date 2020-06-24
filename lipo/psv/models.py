import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Psv(models.Model):

    id = models.UUIDField(_("PSV Id"), primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ManyToManyField("users.UserType", verbose_name=_("P.S.V types"),)
    name = models.CharField(_("Name of PSV"), blank=True, max_length=255)
    sacco = models.ForeignKey("saccos.Sacco", verbose_name=_("Saccos"), on_delete=models.CASCADE,
                              null=True,)
    plate_registration_no = models.CharField(_("Plate Registration Number of PSV"), max_length=255)
    route = models.ManyToManyField("psv_routes.Route", verbose_name=_("Psv Routes Plied by PSV."))
    attribute = models.ManyToManyField("psv.Attribute", verbose_name=_("Psv Attributes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("PSV")
        verbose_name_plural = _("PSVs")

    def __str__(self):
        return self.plate_registration_no

    def get_absolute_url(self):
        return reverse("psv:detail", kwargs={"pk": self.pk})


class PsvType(models.Model):

    TAXI = 'taxi'
    MOTOR_BIKE = 'motor_bike'
    MATATU_MINIBUS = 'matatu_minibus'
    MATATU_BUS = 'matatu_bus'
    BICYCLE = 'bicycle'

    PSV_TYPE = [
        (TAXI, _('Psv is a Taxi')),
        (MOTOR_BIKE, _('Psv is a motorbike')),
        (BICYCLE, _('Psv is a bicycle')),
        (MATATU_MINIBUS, _('Psv is a Matatu Minibus')),
        (MATATU_BUS, _('Psv is a Matatu Bus')),
    ]

   name = models.CharField(_("Name of PSV Type"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Psv Type")
        verbose_name_plural = _("Psv Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("psv_type:detail", kwargs={"pk": self.pk})


class PsvLike(models.Model):
    
    id = models.UUIDField(_("PSV Like Id"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who liked P.S.V"), 
                on_delete=models.CASCADE)
    psv = models.ForeignKey("psv.Psv", verbose_name=_("P.S.V. liked by user"),
                on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Psv Like")
        verbose_name_plural = _("Psv Likes")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("psv_like:detail", kwargs={"pk": self.pk})


class PsvFavourite(models.Model):
    
    id = models.UUIDField(_("PSV Favourite Id"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("user who favourited P.S.V"), 
                on_delete=models.CASCADE)
    psv = models.ForeignKey("psv.Psv", verbose_name=_("P.S.V. favourited by user"),
                on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Psv Like")
        verbose_name_plural = _("Psv Likes")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("psv_favourite:detail", kwargs={"pk": self.pk})



class Attribute(models.Model):

    name = models.CharField(_("Psv Attribute"), max_length=50)

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("attribute:detail", kwargs={"pk": self.pk})
