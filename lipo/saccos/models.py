import uuid
from django.db import models


class Sacco(models.Model):

    id = models.UUIDField(_("Sacco Id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name of Sacco"), max_length=255)

    class Meta:
        verbose_name = _("Sacco")
        verbose_name_plural = _("Saccos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sacco:detail", kwargs={"pk": self.pk})
