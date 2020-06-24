from django.db import models


class Collection(models.Model):

    id = models.UUIDField(_("User Collection Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    creator = models.ForeignKey("users.User", verbose_name=_("Collection Creator"),
                                on_delete=models.CASCADE)
    name = models.CharField(_("Collection Name"), max_length=255)

    class Meta:
        verbose_name = _("Collection")
        verbose_name_plural = _("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection:detail", kwargs={"pk": self.pk})


class PsvCollection(models.Model):

    id = models.UUIDField(_("User Collection Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    psv = models.ForeignKey("psv.Psv", verbose_name=_("Psv In Collection"),
                            on_delete=models.CASCADE)
    collection = models.ForeignKey("user_collections.Collection",
                                   verbose_name=_("Collection containing psvs"),
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("psvcollection")
        verbose_name_plural = _("psvcollections")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("psv_collection:detail", kwargs={"pk": self.pk})
