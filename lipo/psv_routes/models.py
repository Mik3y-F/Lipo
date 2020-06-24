import uuid
from django.db import models


class Route(models.Model):

    id = models.UUIDField(_("PSV Route Id"), primary_key=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField(_("Short Name of PSV Route"), max_length=255)
    long_name = models.CharField(_("Long Name of PSV Route"), max_length=255)
    gtfs_id = models.CharField(_("GTFS Route Id for PSV Route"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Route")
        verbose_name_plural = _("Routes")

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse("route:detail", kwargs={"pk": self.pk})
