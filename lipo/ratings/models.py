import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PsvRating(models.Model):

    id = models.UUIDField(_("P.S.V Rating Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    author = models.ForeignKey("users.Users", verbose_name=_("PSV Rating author"),
                               on_delete=models.CASCADE)
    psv = models.ForeignKey("psv.Psv", verbose_name=_("Psv being Rated"),
                            on_delete=models.CASCADE)
    ratingType = models.ForeignKey("ratings.RatingType", verbose_name=_("PSv rating given"),
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rating:detail", kwargs={"pk": self.pk})


class RatingType(models.Model):

    BAD = 'bad'
    OK = 'ok'
    VERY_GOOD = 'very_good'
    RATING_TYPE = [
        (BAD, _('Experience was bad')),
        (OK, _('Experience was ok')),
        (VERY_GOOD, _('Experience was very good')),
    ]

    name = models.CharField(
        max_length=32,
        choices=RATING_TYPE,
    )
    value = models.PositiveSmallIntegerField(_("Rating Value"), null=True)

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rating_type:detail", kwargs={"pk": self.pk})
