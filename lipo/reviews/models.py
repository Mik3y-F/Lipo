import uuid
from django.db import models
from django.utils.text import slugify


class PsvReview(models.Model):

    id = models.UUIDField(_("Review Id"), primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("users.Review", verbose_name=_("user_reviews"),
                               on_delete=models.CASCADE)
    psv = models.ForeignKey("psv.Psv", verbose_name=_("reviewed P.S.V"), on_delete=models.CASCADE)
    body = models.CharField(_("PSV Review Body"), blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return slugify(f'{self.author.get_full_name_slug} {self.psv.plate_registration_no} review')

    def get_absolute_url(self):
        return reverse("Review_detail", kwargs={"pk": self.pk})


def get_image_filename(instance, filename):
    psv_id = instance.review.psv
    author_id = instance.review.author
    return f"user/{author_id}/psv_images/{psv_id}"


class ReviewImage(models.Model):

    id = models.UUIDField(_("Review Image Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    review = models.ForeignKey("reviews.psvReview", verbose_name=_("Review whose image is attached"),
                               id=instance.post.id
                               on_delete=models.CASCADE)
    psv_image = models.ImageField(_("Review Image"), upload_to=get_image_filename,
                                  height_field=None,
                                  width_field=None, max_length=100)

    class Meta:
        verbose_name = _("ReviewImage")
        verbose_name_plural = _("ReviewImages")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("ReviewImage_detail", kwargs={"pk": self.pk})
